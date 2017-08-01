# encoding: utf-8
import requests,json
import config
from flask import render_template,request,redirect
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


@app.route(config.CALLBACK,methods = {'POST','GET'})
def login_gitlab():
    code = request.args.get('code')
    playload = {
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'code': code,
        'grant_type': config.GRANT_TYPE,
        'redirect_uri': config.REDIRECT_URI
    }
    r = requests.post(config.POST_TOKEN_URL,playload)
    x = json.loads(r.text)
    token = {
        'access_token': x['access_token']
    }
    y = requests.get(config.GITLAB_API_URL+'user',token)
    return y.text

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
