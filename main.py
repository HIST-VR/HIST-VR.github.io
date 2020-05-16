import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://www.citrus.ua/noutbuki-i-ultrabuki/'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_page_count(html):
    soup = BeautifulSoup(html, features='lxml')
    pagination = soup.find('div', class_='pagination-container')
    return int(pagination.find_all('a')[-2].text)

def parse(html):
    soup = BeautifulSoup(html, features='lxml')

    table = soup.find('div', class_='catalog__items')

    projects= []

    for row in table.find_all(class_='product-card__overview'):

         title = row.find_all('div', class_='product-card__name')
         price = row.find_all('div', class_='prices__price')
         projects.append({

             # 'title': title[0].a.text.strip(),
             'title': title[0].a['title'],
             'price': price[0].span.text.strip(),

             })


    return projects



def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Название', 'Цена'))

        for project in projects:
            writer.writerow((project['title'], (project['price'])))


def main():

    page_count = get_page_count(get_html(BASE_URL))
    print('Всего страниц:', page_count)

    projects = []

    for page in range(1, page_count):
        print('Парсинг %d%%' % (page / page_count * 100))
        projects.extend(parse(get_html(BASE_URL + '?page_%d' % page)))
    print("Парсинг 100%")

    for project in projects:
        print(project)

    save(projects, 'projects.cvs')


if __name__ == '__main__':
    main()
