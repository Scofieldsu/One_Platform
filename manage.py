# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 17:05
@Author : Yu Yuan

"""

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import config
from ext import db
from models import *
import click

app = Flask(__name__)
app.config.from_object(config)

migrate = Migrate(app, db)

@app.cli.command()
def initdb():
    db.session.commit()
    db.drop_all()
    db.create_all()
    click.echo('Init Finished!')
