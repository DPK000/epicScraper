import requests

proxy = '172.105.184.208:8001'

r = requests.get('https://httpbin.org/ip', proxies={'http':proxy, 'https':proxy}, timeout=3)

print(r.status_code)