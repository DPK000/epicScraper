import requests
from bs4 import BeautifulSoup
import pymysql.cursors

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    location_elemen = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='',
                           database='blog',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    our_list = [(title_element.text.strip(), company_element.text.strip(), location_element.text.strip(),
                 location_elemen.text.strip())]
    cur = conn.cursor()
    sql = ("INSERT INTO wiki (title, location, price, area) VALUES (%s, %s, %s, %s)")
    try:
        cur.executemany(sql, our_list)
        conn.commit()
        print('new city inserted')
    except:
        conn.rollback()
        cur.execute("SELECT * FROM wiki")
        for x in cur:
            print(x)
            cur.close()
            conn.close()
    finally:
        conn.close()

# DIT WERKT
# try:
#
#     with con.cursor() as cur:
#
#         cur.execute('SELECT * FROM wiki')
#
#         rows = cur.fetchall()
#
#         for row in rows:
#             print(row['id'], row['name'])
#
# finally:
#
#     con.close()
