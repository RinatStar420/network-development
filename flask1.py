"""Пакет Flask включает в себя библиотеку package WSGI и билиотеку шаблонов jinja2.
Установить Flask можно с помощью команды pip install flask.

Этот пример демонстрирует, как передавать аргументы в URL и использовать их."""

from flask import Flask
"""Во Flask папка по умолчанию для статическиз файлов называется static, и URL для таких файлов тож начинается
со /static. Изменим папку на '.'(текущая папка) и префикс URL на ''(пустой), чтобы позволить URl / отображать файл
index.html"""
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def home():
    return app.send_static_file('index.html')
@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing
app.run(port=9999, debug=True)
# установка параметра debug=True активизирует также автоматическую перезагрузку
