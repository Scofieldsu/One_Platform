# encoding: utf-8

from flask import Flask
from flaskapi.api import api
import config
import tools.exchange_rate
import apis.login_signup

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api.as_blueprint(url='/api'))
    app.config.from_object(config)
    from models import db
    db.init_app(app)
    return app