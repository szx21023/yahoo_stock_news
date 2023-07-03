import requests
from bs4 import BeautifulSoup as bs

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