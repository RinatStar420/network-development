""" Для установки bottle необходимо выполнить комманду pip install bottle
Следующий код запустит тестовый веб-сервер и вернет текстовою строку, когда браузер обратиться
по URL http://localhost:9999"""

from bottle import route, run
@route('/')
# Декоратор route используется, чтобы связать URL  со следующей функцией home
# в этом примере '/' (домашняя страница) обрабатывается функцией home()
def home():
    return "It isn't fancy, but it's my homepage"


run(host='localhost', port=9999)
# функция run() запускает встроенный тестовый сервер Bottle