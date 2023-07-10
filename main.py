from datetime import datetime

from config import host_url, stock_list, region
from page_crawler import yahoo_crawler
from connect_db import stock_news
from utils import strip_colon

sql_query = "SELECT title FROM news"
existed_title_l = set(row[0] for row in stock_news.select(sql_query))
for stock_code in stock_list:
    news_l = yahoo_crawler.parser_stock(host_url, stock_code, region)

    for news in news_l:
        crawl_time = str(datetime.now())
        if news['title'] in existed_title_l:
            continue
        news['stock_code'] = stock_code
        news['post_content'] = strip_colon(news['post_content'])
        news['crawl_time'] = crawl_time
        stock_news.insert(**news)
        print('----------------------------')

# 關閉瀏覽器
yahoo_crawler.driver.quit()

# 擷取查詢結果
# for row in results:
#     print(type(row))
