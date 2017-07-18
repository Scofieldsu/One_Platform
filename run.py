# encoding: utf-8
from flask import render_template
from appmanage import create_app
from werkzeug.contrib.fixers import ProxyFix


app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
