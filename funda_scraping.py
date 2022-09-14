from bs4 import BeautifulSoup
import requests
import re

url = "https://kamernet.nl/en/for-rent/rooms-amsterdam"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

lists = doc.find_all(class_="tile-wrapper ka-tile")


for list in lists[:10]:
    price = list.find('div', class_="tile-rent").text.replace('\n', '')
    surface = list.find('div', class_="tile-surface").text.replace('\n', '')
    city = list.find('div', class_="tile-city").text.replace('\n', '')
    type = list.find('div', class_="tile-room-type").text.replace('\n', '')

    info = [price, surface, city, type]

data = {
    "price": price,
    "surface":surface,
    "city":city,
    "type":type
}

print(data)



# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# from datetime import datetime
# import pytz
#
# tz = pytz.timezone('Europe/Amsterdam')
# time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
#
# cred = credentials.Certificate("houseapp-cf2d1-firebase-adminsdk-wzesx-5e7a2d3ada.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()
#
# def save(collection_id, document_id, data):
#     db.collection(collection_id).document(document_id).set(data)
#
# save(
#     collection_id = "woningData",
#     document_id = f"{time}",
#     data=data
# )