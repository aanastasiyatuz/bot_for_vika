import requests
from bs4 import BeautifulSoup


url = 'http://cbd.minjust.gov.kg/act/view/ru-ru/111565'

def parsing(url):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    text_ = soup.find('div', class_="WordSection1").find_all('p', class_="MsoNormal")
    indexes = []
    for p in text_:
        if p.text.split(' ')[0] == 'Статья':
            index = text_.index(p)
            indexes.append(index)
    return filter(text_, indexes)

def filter(text_, indexes):
    for i in indexes:
        try:
            next_ = indexes[i+1]
        except IndexError:
            return list_
        list_ = text_[i+1: next_]
        for a, b in enumerate(list_):
            if a == indexes[-1]:
                print('a')
            
            try:
                list_[a] = list_[a].text.replace('\r\n', '')
            except AttributeError:
                list_[a] = list_[a].replace('\r\n', '')
            
parsing(url)