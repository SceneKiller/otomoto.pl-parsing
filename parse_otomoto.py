import csv

import requests
from bs4 import BeautifulSoup
import fake_useragent
from time import sleep


main_link = 'https://www.otomoto.pl/osobowe?search%5Border%5D=filter_float_price%3Adesc'


def setup_session():
    session = requests.Session()
    session.headers.update({
        'user-agent': fake_useragent.UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    })
    return session


def get_links():
    links = []
    session = setup_session()
    response = session.get(main_link)
    soup = BeautifulSoup(response.text, 'lxml')
    block = soup.find('div', attrs={'data-testid': 'search-results'})
    items = block.find_all('article')
    for item in items:
        try:
            item_data = item.find('h2', class_='etydmma0 ooa-ezpr21')
            item_link = item_data.find('a').get('href')
        except AttributeError:
            continue
    return links


def scrape_data(links):
    global session
    for link in links:
        response = session.get(link)
         


def save_to_csv(data):
    with open('auto.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Название', 'Сcылка'])
        writer.writerows(data)


def main():
    links = get_links()
    data =
    save_to_csv(data)


if __name__ == "__main__":
    main()
