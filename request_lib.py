""" За пределами стандартной библиотеки urllib.request и json сущетвует строронняя библиотекка request.
Для установка - pip install requests"""
import requests
url = 'http://www.aphorisme.ru/random/?=2329'
resp = requests.get(url)
print(resp.text)