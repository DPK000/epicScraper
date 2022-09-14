import requests
import csv
import concurrent.futures
from bs4 import BeautifulSoup
import pymysql.cursors

proxylist = []

with open('proxyrotator.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])


def extract(proxy):
    try:
        r = requests.get('https://www.pararius.com/apartments/amsterdam?ac=1', proxies={'http': proxy, 'https': proxy},
                         timeout=2)
        soup = BeautifulSoup(r.content, "html.parser")
        lists = soup.find_all('section',
                              class_="listing-search-item listing-search-item--list listing-search-item--for-rent")

        for list in lists:
            title = list.find('a', class_="listing-search-item__link listing-search-item__link--title")
            location = list.find('div', class_="listing-search-item__sub-title")
            price = list.find('div', class_="listing-search-item__price")
            area = list.find('li',class_="illustrated-features__item illustrated-features__item--surface-area")
            print(title.text.strip())
            print(location.text.strip())
            print(price.text.strip())
            print(area.text.strip())
            print()
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='',
                                   database='blog',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
            info = [(title.text.strip(), location.text.strip(), price.text.strip(), area.text.strip())]
            cur = conn.cursor()
            sql = ("INSERT INTO wiki (title, location, price, area) VALUES (%s, %s, %s, %s)")
            try:
                cur.executemany(sql, info)
                conn.commit()
                print('new data added niceeeeeee')
            except:
                conn.rollback()
                cur.execute("SELECT * FROM wiki")
                for x in cur:
                    print(x)
                    cur.close()
                    conn.close()
            finally:
                conn.close()


    except:
        pass
        return proxy


with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract, proxylist)
