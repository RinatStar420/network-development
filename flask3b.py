"""Также возможно передать аргументы как параметры команды GET
Когда команда GET используется в URL, любые аргументы должны передаваться в формате &key1=val1&key2=val2&..."""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/echo/')
# Декоратор используется, чтобы связать URL  со следующей функцией echo
def echo():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask3.html', thing=thing, place=place)


app.run(port=9999, debug=True)
