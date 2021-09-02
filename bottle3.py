""" Этот пример демонстрирует, как передавать аргументы в URL и использовать их."""

from bottle import route, run, static_file
@route('/')
def home():
    return static_file('index.html', root='.')
@route('/echo/<thing>')
# отвечает за передачу строкового аргумента в функцию echo
def echo(thing):
    # echo - функция, в которую необходимо передавать строковой аргумент через URL.
    return "Say hello to my little friend: %s!" % thing
run(host='localhost', port=9999)
# Конструкция <thing> в маршруте означает, что все, что находится в URL после /echo/, присваивается
# строковому аргументу thing, который передается в функцию echo()