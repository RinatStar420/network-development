""" Теперь вместо создания текста домашней страницы в коде создадим отдельный html файл, который называется index.html
и содержит строку: My <b>new</b> and <i>improved</i> home page!!!
Укажем Bottle возвращать содержимое этого файла, когда запрашивается домашняя страница """

from bottle import route, run, static_file
@route('/')
def main():
    return  static_file('index.html', root='.')
# В вызове static_file() я хочу получить файл index.html из каталога, указанноего в root(в нашем случае в '.', текущем
# каталоге).
run(host='localhost', port=9999)