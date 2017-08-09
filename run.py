# encoding: utf-8
import requests,json
import config
from flask import render_template,request
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
    from models.Setting import Setting
    setting = Setting.query.filter_by(application_name=config.APPLICATION).first()
    code = request.args.get('code')
    playload = {
        'client_id': setting.client_id,
        'client_secret': setting.client_secret,
        'code': code,
        'grant_type': config.GRANT_TYPE,
        'redirect_uri': setting.redirect_uri
    }
    r = requests.post(setting.gitlab_url+config.POST_TOKEN_URL,playload)
    x = json.loads(r.content)
    token = {
        'access_token': x['access_token']
    }
    y = requests.get(setting.gitlab_url+config.GITLAB_API_URL+'user',token)
    user = json.loads(y.content)
    from models.User import User
    query_user = User.query.filter_by(email=user['email']).first()
    if query_user :
        user['id'] = query_user.id
    else:
        sign_up_user = User(user['name'], user['email'], config.PWD)
        sign_up_user.save()
        user['id'] = User.query.filter_by(email=user['email']).first().id
    return render_template('transfer.html', user = user,login_url = setting.redirect_server+config.LOGIN_URL)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
