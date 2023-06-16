from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 創建一個Chrome瀏覽器實例
driver = webdriver.Chrome()

# 打開Google首頁
driver.get("https://tw.stock.yahoo.com/quote/2330.TW")

# 等待搜尋結果頁面載入完成
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
element = soup.find('div', {
    'id': 'YDC-Stream'})
elements = element.find_all('li', {'class': 'js-stream-content Pos(r)'})
for element in elements:
    # filter ad
    if element.find('div', {'class': 'controller gemini-ad native-ad-item Feedback Pos(r)'}):
        continue

    tags = element.find_all("span")
    for tag in tags:
        print(tag)

    tags = element.find_all("h3")
    for tag in tags:
        print(tag)

    tags = element.find_all("p")
    for tag in tags:
        print(tag)

    urls = element.find_all("a")
    for url in urls:
        print(url.get("href"))

    print('----------------------------')

# 關閉瀏覽器
driver.quit()
