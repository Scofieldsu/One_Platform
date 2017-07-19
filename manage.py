# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 17:05
@Author : Yu Yuan

"""

import click
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager, Shell
from run import app
from models import db

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

from models import *


@manager.command
def init_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    click.echo('Init db Finished!')

@migrate.configure
def configure_alembic(config):
    return config

if __name__ == '__main__':
    manager.run()