""" Также можно использовать оператор словаря **, чтобы передать несколько аргументов в шаблон с помощью
одного словаря"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html', **kwargs)


app.run(port=9999, debug=True)
