# gcloud auth application-default login
import os
from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
from config import gcp_db_project, gcp_db_region, gcp_db_instance, gcp_db_user, gcp_db_password, gcp_db_database, \
    GOOGLE_APPLICATION_CREDENTIALS

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

def insert(title, author, post_time, post_content, url, source, crawl_time):
    sql_insert = f"""INSERT INTO news (
            title, author, post_time, post_content, url, source, crawl_time) VALUES (
            '{title}', '{author}', '{post_time}', '{post_content}', '{url}', '{source}', '{crawl_time}')"""
        
    insert_stmt = sqlalchemy.text(
        sql_insert,
    )

    cursor = pool.connect()
    cursor.execute(insert_stmt)
    cursor.commit()

# insert statement
title = 'test'
author = 'herry'
post_time = '2023/06/26 21:17:00'
post_content = 'hello'
url = 'tcp:172.0.0.1'
source = 'remote'
crawl_time = '2023/09/26 21:17:00'
insert(title, author, post_time, post_content, url, source, crawl_time)