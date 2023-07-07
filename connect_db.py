# gcloud auth application-default login
from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
import os

from config import db_host, db_port, db_user, db_password, db_database, \
    gcp_db_project, gcp_db_region, gcp_db_instance, gcp_db_user, gcp_db_password, gcp_db_database, \
    GOOGLE_APPLICATION_CREDENTIALS

def generate_connector(gcp_mode=False):
    def gcp_connection():
        # initialize Connector object
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS
        connector = Connector()

        # function to return the database connection
        def getconn() -> pymysql.connections.Connection:
            conn: pymysql.connections.Connection = connector.connect(
                f"{gcp_db_project}:{gcp_db_region}:{gcp_db_instance}",
                "pymysql",
                user=gcp_db_user,
                password=gcp_db_password,
                db=gcp_db_database
            )
            return conn

        # create connection pool
        pool = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=getconn,
        )
        return pool.connect(), pool

    def local_connection():
        # 連接到 MySQL 資料庫
        connection = pymysql.connect(
            host = db_host,
            port = db_port,
            user = db_user,   # 使用者名稱
            password = db_password,  # 使用者密碼
            database = db_database   # 資料庫名稱
        )
        return connection.cursor(), connection

    return gcp_connection() if gcp_mode else local_connection()

# 建立游標物件
class Stock_news:
    def __init__(self, cursor, connection=None, gcp_mode=False):
        self.cursor = cursor
        self.connection = connection
        self.gcp_mode = gcp_mode

    def insert(self, title, author, post_time, post_content, url, source, crawl_time):
        sql_query = f"""INSERT INTO news (title, author, post_time, post_content, url, source, crawl_time) VALUES ('{title}', '{author}', '{post_time}', '{post_content}', '{url}', '{source}', '{crawl_time}')"""
        self.cursor.execute(self.transform(sql_query))
        self.commit()

    def select(self, sql_query):
        results = self.fetch_all(sql_query)
        return results

    def commit(self):
        if self.gcp_mode:
            self.cursor.commit()  # 提交修改
        else:
            self.connection.commit()

    def fetch_all(self, sql):
        if self.gcp_mode:
            return self.cursor.execute(self.transform(sql)).fetchall()
        self.cursor.execute(self.transform(sql))
        return self.cursor.fetchall()

    def transform(self, sql):
        return sqlalchemy.text(sql) if self.gcp_mode else sql

gcp_mode = False
cursor, connection = generate_connector(gcp_mode)
stock_news = Stock_news(cursor, connection, gcp_mode)
