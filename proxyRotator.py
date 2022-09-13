import requests
import csv
import concurrent.futures

proxylist = []

with open('proxyrotator.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])


def extract(proxy):
    try:
        r = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=2)
        print(r.json(), ' - working')
    except:
        pass
        return proxy

    extract('47.88.6.186:30001')


with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract, proxylist)
