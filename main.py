from datetime import datetime

from config import host_url, stock_code, region
from page_crawler import yahoo_crawler
from connect_db import stock_news

# l = yahoo_crawler.parser_stock(host_url, stock_code, region)

# for news in l:
#     crawl_time = str(datetime.now())
#     stock_news.insert(news['title'], news['author'], news['post_time'], news['post_content'], news['url'], news['source'], crawl_time)
#     print('----------------------------')

# # 關閉瀏覽器
# yahoo_crawler.driver.quit()
stock_news.select()
