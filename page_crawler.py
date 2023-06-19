import requests
from bs4 import BeautifulSoup as bs

url = 'https://tw.stock.yahoo.com/news/%E5%8F%B0%E7%A9%8D%E9%9B%BB%E5%8F%97%E6%83%A0%E5%85%88%E9%80%B2%E8%A3%BD%E7%A8%8B%E6%BC%B2%E5%83%B9-%E7%A0%94%E8%AA%BF%E4%BC%B0%E6%98%8E%E5%B9%B4%E7%87%9F%E6%94%B6%E5%8F%AF%E6%9C%9B%E8%B7%B3%E5%A2%9E22-5-092545480.html'
def parser_content(url):
    info = requests.get(url)
    soup = bs(info.text,"lxml")

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
print(parser_content(url))