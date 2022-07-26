import requests
from bs4 import BeautifulSoup

url = 'http://www.blog.pythonlibrary.org/'

def get_articles():
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.findAll('h1')
    articles = {i.a['href']: i.text.strip() for i in pages if i.a}
    for article in articles:
        s = '{title}: {url}'.format(title=articles[article].encode('utf-8'), url=article)
        print(s)
    return articles

if __name__ == '__main__':
    articles = get_articles()
