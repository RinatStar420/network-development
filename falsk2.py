"""Flask содержит jinja2 - более широкую систему шаблонов (чем Bottle). Подготовлю пример одновременного использования
 jinja2  и flask.
 Создам папку templates и внутри файл flask2.html.
 Далее напишу серверный код, который получает вышеуказанный шаблон, заполняет значение аргумента thing, который мы
 передаем и отрисовывает его как HTML."""

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)
# Аргумент thing=thing означает, что для передачи переменной с именем thing в шаблон эта переменная содержит значение
# строки thing
app.run(port=9999, debug=True)