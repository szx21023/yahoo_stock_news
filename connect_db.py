import pymysql

from config import db_host, db_port, db_user, db_password, db_database

# 連接到 MySQL 資料庫
connection = pymysql.connect(
    host = db_host,
    port = db_port,
    user = db_user,   # 使用者名稱
    password = db_password,  # 使用者密碼
    database = db_database   # 資料庫名稱
)

# 建立游標物件
class Stock_news:
    def __init__(self, connection):
        self.cursor = connection.cursor()

    def insert(self, title, author, post_time, post_content, url, source, crawl_time):
        sql_insert = """INSERT INTO news (
        title, author, post_time, post_content, url, source, crawl_time) VALUES (
        %s, %s, %s, %s, %s, %s, %s)"""

        values = (title, author, post_time, post_content, url, source, crawl_time)

        self.cursor.execute(sql_insert, values)
        connection.commit()  # 提交修改

    def select(self):
        # 執行 SQL 查詢
        sql_query = "SELECT * FROM news"
        self.cursor.execute(sql_query)

        # 擷取查詢結果
        results = self.cursor.fetchall()
        for row in results:
            print(row)

stock_news = Stock_news(connection)

title = 'test'
author = 'herry'
post_time = '2023/06/26 09:59:00'
post_content = 'hello'
url = 'https:127.0.0.1'
source = 'local'
crawl_time = '2023/06/26 10:0:00'
stock_news.insert(title, author, post_time, post_content, url, source, crawl_time)
stock_news.select()