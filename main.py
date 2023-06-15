from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 創建一個Chrome瀏覽器實例
driver = webdriver.Chrome()

# 打開Google首頁
driver.get("https://tw.stock.yahoo.com/quote/2330.TW")

# 等待搜尋結果頁面載入完成
driver.implicitly_wait(10)

# 找到所有的搜索結果元素
element = driver.find_element(By.ID, "YDC-Stream")

link_elements = element.find_elements(By.TAG_NAME, "a")
# 提取並打印連結的URL
for link_element in link_elements:
    parent_element = link_element.find_element(By.XPATH, "..")
    print(parent_element.text)
    url = link_element.get_attribute("href")
    print(url)

# 關閉瀏覽器
driver.quit()
