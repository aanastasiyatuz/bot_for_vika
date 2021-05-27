import requests
from bs4 import BeautifulSoup


def parsing():
    url = 'http://cbd.minjust.gov.kg/act/view/ru-ru/111565'
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    text_ = soup.find('div', class_="WordSection1").find_all('p', class_="MsoNormal")
    indexes = 0
    for p in text_:
        if p.text.split(' ')[0] == 'Статья':
            index = text_.index(p)
            indexes = index
            break
    return filter(text_[indexes:])

def filter(text_):
    for i in text_:
        text_[text_.index(i)] = i.text
    return text_[:20]

            
parsing()
