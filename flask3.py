""" Созданим новый файд flask3.html с добавлением второго шаблона для аргумента URL (первый шаблон thing,
второй шаблон place)
Второй аргумент в URL, echo, можно передавать множеством способов.
С помощью следующего метода просто расширяем URL """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/echo/<thing>/<place>')
# Декоратор используется, чтобы связать URL  со следующей функцией echo
def echo(thing, place):
    return render_template('flask3.html', thing=thing, place=place)


app.run(port=9999, debug=True)
