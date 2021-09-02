import urllib.request as ur

url = 'http://www.aphorisme.ru/random/?=2329'
conn = ur.urlopen(url)
print(conn)
