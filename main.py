from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 創建一個Chrome瀏覽器實例
driver = webdriver.Chrome()

# 打開Google首頁
driver.get("https://www.google.com")

# 找到搜尋框元素
search_box = driver.find_element(By.NAME, "q")

# 在搜尋框輸入關鍵字
search_box.send_keys("OpenAI")

# 按下Enter執行搜索
search_box.send_keys(Keys.RETURN)

# 等待搜尋結果頁面載入完成
driver.implicitly_wait(10)

# 找到所有的搜索結果元素
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")

# 打印搜索結果標題和網址
for result in search_results:
    title = result.find_element(By.CSS_SELECTOR, "h3").text
    url = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    print(f"標題: {title}")
    print(f"網址: {url}")
    print()

# 關閉瀏覽器
driver.quit()
