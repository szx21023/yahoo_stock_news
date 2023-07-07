from datetime import datetime

from config import host_url, stock_code, region
from page_crawler import yahoo_crawler
from connect_db import stock_news

sql_query = "SELECT title FROM news"
title_l = set(row[0] for row in stock_news.select(sql_query))
news_l = yahoo_crawler.parser_stock(host_url, stock_code, region)

for news in news_l:
    crawl_time = str(datetime.now())
    if news['title'] in title_l:
        continue
    stock_news.insert(news['title'], news['author'], news['post_time'], news['post_content'], news['url'], news['source'], crawl_time)
    print('----------------------------')

# 關閉瀏覽器
yahoo_crawler.driver.quit()

# 擷取查詢結果
# for row in results:
#     print(type(row))
