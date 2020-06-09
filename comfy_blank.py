import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://comfy.ua/notebook/?p=1'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    soup = BeautifulSoup(html, features='lxml')
    pagination = soup.find('div', class_='pagination-container')
    return int(pagination.find_all('a')[-2].text)


def parse(html):
    soup = BeautifulSoup(html, features='lxml')

    table = soup.find('div', class_='js-products-list-wrap')
    projects = []

    for row in table.find_all('div', class_='products-list js-item-list'):
        print(row)


        # title = row.find_all('div', class_='goods-tile__heading')
        # price = row.find_all('div', class_='goods-tile__price-value')
        # projects.append({
        #     # 'title': title[0].a.text.strip(),
        #     'title': title[0].a['title'],
        #     'price': price[0].span.text.strip(),
        # })

    return projects


#
# def save(projects, path):
#     with open(path, 'w') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(('Название', 'Цена'))
#
#         for project in projects:
#             writer.writerow((project['title'], (project['price'])))


def main():
    # page_count = get_page_count(get_html(BASE_URL))
    # print('Всего страниц:', page_count)
    #
    projects = []
    #
    # for page in range(1, page_count):
    #     print('Парсинг %d%%' % (page / page_count * 100))
    #     projects.extend(parse(get_html(BASE_URL + '?page_%d' % page)))
    # print("Парсинг 100%")
    #
    # for project in projects:
    #     print(project)
    #
    # save(projects, 'rozetka_parse.cvs')

    projects.extend(parse(get_html(BASE_URL)))

    print(projects)


if __name__ == '__main__':
    main()
