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
    result = dict()
    error = request.args.get('error')
    if error:
        return render_template('index.html')
    from models.Setting import Setting
    from models.Configuration import Configuration
    configuration = Configuration.query.all()
    if not configuration:
        result["msg"] = "cann't find configuration"
        return result
    elif len(configuration) == 1:
        application_name = configuration[0].application_name
    else:
        result["msg"] = "configuration error not one"
        return result
    setting = Setting.query.filter_by(application_name=application_name).first()
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
        query_user.access_token = x['access_token']
        query_user.save()
    else:
        sign_up_user = User(user['name'], user['email'], config.PWD)
        sign_up_user.access_token = x['access_token']
        sign_up_user.save()
        user['id'] = User.query.filter_by(email=user['email']).first().id
    return render_template('transfer.html', user=user,login_url=setting.redirect_server+config.LOGIN_URL)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
