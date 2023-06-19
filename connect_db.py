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
cursor = connection.cursor()

sql_insert = """INSERT INTO news (
title, author, post_time, post_content, url, source, crawl_time) VALUES (
%s, %s, %s, %s, %s, %s, %s)"""
values = ('test', 'herrt', '2023/06/19 08:45:00', 'hello', 'https:127.0.0.1', 'local', '2023/06/19 08:46:00')

cursor.execute(sql_insert, values)
connection.commit()  # 提交修改

# 執行 SQL 查詢
sql_query = "SELECT * FROM news"
cursor.execute(sql_query)

# 擷取查詢結果
results = cursor.fetchall()
for row in results:
    print(row)

# 關閉連接
cursor.close()
connection.close()