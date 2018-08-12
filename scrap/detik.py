import bs4
from urllib.request import urlopen
import pandas as pd
import datetime

page = 'https://www.detik.com/pemilu/'
articles_num = 464

def fetch_page(page, page_num):
    page = urlopen("{}/{}".format(page, page_num))
    soup = bs4.BeautifulSoup(page, 'html.parser')
    
    articles = soup.findAll('article')
    articles[0].find('img')['title']
    title = []
    for article in articles:
        title.append(article.find('img')['title'])
    return title

def fetch_all(articles_num):
    title = []
    for page_num in range(1,articles_num + 1):
        print(page_num)
        title = title + fetch_page(page, page_num)
    return title

def make_dataframe(title_list):
    columns = ['titles','sources']
    df = pd.DataFrame(columns=columns)
    data = pd.DataFrame({"titles": title, "sources": ["detik.com" for i in range(len(title))]})
    df = df.append(data)
    return df

def start_scrap():
    title = fetch_all
    df = make_dataframe(title)

    now = datetime.datetime.now()
    df.to_csv('detik_{}.csv'.format(now.strftime("%Y-%m-%d")))
    return df