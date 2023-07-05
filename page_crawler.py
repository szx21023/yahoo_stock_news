from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

class YahooCrawler:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # 創建一個Chrome瀏覽器實例
        self.driver = webdriver.Chrome(options=options)

    def parser_stock(self, host_url, stock_code, region):
        # 打開Google首頁
        self.driver.get(f"{host_url}/{stock_code}.{region}")

        # 等待搜尋結果頁面載入完成
        self.driver.implicitly_wait(10)

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        elements = soup.find_all('li', {'class': 'js-stream-content Pos(r)'})
        l = []
        for element in elements:
            # filter ad
            if element.find('div', {'class': 'controller gemini-ad native-ad-item Feedback Pos(r)'}):
                continue

            # source web, post_time
            tags = element.find_all("span")
            source = ''.join([tag.text for tag in tags[:1]])

            # # title
            # tags = element.find_all("h3")
            # title = ''.join([tag.text for tag in tags])

            # # outline
            # tags = element.find_all("p")
            # for tag in tags:
            #     print(tag)

            # link_url
            tags = element.find_all("a")
            url = tags[0].get("href")

            attr = self.parser_content(url)
            attr['source'] = source
            l.append(attr)
        return l

    @staticmethod
    def parser_content(url):
        info = requests.get(url)
        soup = BeautifulSoup(info.text,"lxml")

        article = soup.find('article', {'role': 'article'})
        title = article.find('h1', {'data-test-locator': 'headline'})
        author = article.find('span', {'class': 'caas-author-byline-collapse'})
        post_time = article.find('time', {'class': 'caas-attr-meta-time'}).get('datetime')
        post_content = article.find('div', {'class': 'caas-body'})
        return {
            'url': url,
            'title': title.text,
            'author': author.text,
            'post_time': post_time,
            'post_content': post_content.text
        }

yahoo_crawler = YahooCrawler()