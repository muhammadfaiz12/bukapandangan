import bs4
from urllib.request import urlopen
import time
import pandas as pd
import datetime

page = 'https://indeks.kompas.com/tag/pilpres-2019'

def fetch_page(page, page_num):
    page = urlopen("{}/desc/{}".format(page, page_num))
    soup = bs4.BeautifulSoup(page, 'html.parser')
    
    articles = soup.findAll('div', attrs={'class':"article__list__title"})
    title = []
    for article in articles:
        title.append(article.find('h3').text)
    return title

def fetch_all(articles_num):
    counter = 1
    title_all = []
    title = fetch_page(page,counter)
    title_all = title
    while len(title) > 0:
        try:
            counter = counter + 1
            print(counter, len(title))
            title = fetch_page(page, counter)
            title_all = title_all + title 
            time.sleep(0.1)
        except ConnectionResetError:
            counter = counter - 1
    return title_all

def make_dataframe(title_list):
    columns = ['titles','sources']
    df = pd.DataFrame(columns=columns)
    data = pd.DataFrame({"titles": title, "sources": ["kompas.com" for i in range(len(title))]})
    df = df.append(data)
    return df

def start_scrap():
    title = fetch_all
    df = make_dataframe(title)

    now = datetime.datetime.now()
    df.to_csv('kompas_{}.csv'.format(now.strftime("%Y-%m-%d")))
    return df