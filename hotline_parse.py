import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'https://hotline.ua/computer/noutbuki-netbuki/'



def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    soup = BeautifulSoup(html, features='lxml')
    pagination = soup.find('div', class_='pages-list cell-sm')
    return int(pagination.find_all('a')[-1].text)


def parse(html):
    soup = BeautifulSoup(html, features='lxml')

    table = soup.find('ul', class_='products-list cell-list')

    projects = []
    try:
        for row in table.find_all(class_='product-item'):
            #print(row)
            title = row.find_all('div', class_='item-info')
            print(title)
            price = (row.find_all('div', class_='price-md'))
            price_range = (row.find('div', class_='text-sm'))
            img = (row.find('img'))
            try:
                # for i in images:
                #     img = (i['src'])
                projects.append({
                    'title': title[0].a.text.strip(),
                    'price': (price[0].span.text),
                    'price_range': price_range.text,
                    'image': 'https://hotline.ua/' + img['src'],
                })
            except:
                None

        return projects
    except:
        None



def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Name', 'Price', 'Price range', 'Image'))

        for project in projects:
            writer.writerow((project['title'], (project['price']), project['price_range'], project['image']))


def main():
    #page_count = get_page_count(get_html(BASE_URL))
    page_count = 2
    print('Всего страниц:', page_count)

    projects = []

    for page in range(1, page_count):
        print('Парсинг %d%%' % (page / page_count * 100))
        projects.extend(parse(get_html(BASE_URL + '?p=%d' % page)))
    print("Парсинг 100%")

    # for project in projects:
    #     print(project)


    save(projects, 'hotline_parse.cvs')

    #print(projects)


if __name__ == '__main__':
    main()
