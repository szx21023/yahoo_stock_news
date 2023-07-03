from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from config import host_url, stock_code, region

options = Options()
options.add_argument('--headless')

# 創建一個Chrome瀏覽器實例
driver = webdriver.Chrome(options=options)

# 打開Google首頁
driver.get(f"{host_url}/{stock_code}.{region}")

# 等待搜尋結果頁面載入完成
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# element = soup.find('div', {
#     'id': 'YDC-Stream'})
elements = soup.find_all('li', {'class': 'js-stream-content Pos(r)'})
for element in elements:
    # filter ad
    if element.find('div', {'class': 'controller gemini-ad native-ad-item Feedback Pos(r)'}):
        continue

    # source web, post_time
    tags = element.find_all("span")
    for tag in tags:
        print(tag)

    # title
    tags = element.find_all("h3")
    for tag in tags:
        print(tag)

    # outline
    tags = element.find_all("p")
    for tag in tags:
        print(tag)

    # link_url
    urls = element.find_all("a")
    for url in urls:
        print(url.get("href"))

    print('----------------------------')

# 關閉瀏覽器
driver.quit()
