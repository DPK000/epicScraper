from bs4 import BeautifulSoup
import requests

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)
doc = BeautifulSoup(page.content, "html.parser")

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('section', class_="listing-search-item listing-search-item--list listing-search-item--for-rent")

for list in lists:
    title = list.find('a', class_="listing-search-item__link listing-search-item__link--title").text.replace('\n', '')
    location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
    price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
    area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace(
        '\n', '')

    info = [title, location, price, area]

    print(info)
