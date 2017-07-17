# encoding: utf-8

from flask import Flask
from flaskapi.api import api
import config
import tools.exchange_rate
from flask_sqlalchemy import SQLAlchemy
from ext import BaseModel


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api.as_blueprint(url='/api'))
    app.config.from_object(config)
    db = SQLAlchemy(app,model_class=BaseModel)
    db.init_app(app)
    # db.create_all(app)
    return app