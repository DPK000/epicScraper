from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price




data = {
    "name": fixed_name,
    "Price": fixed_price
}
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
#     collection_id = "crypto",
#     document_id = f"{time}",
#     data=data
# )
#
