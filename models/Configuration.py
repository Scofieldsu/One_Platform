# -*- coding: utf-8 -*-
"""
@Time : 2017/8/10 10:33
@Author : Yu Yuan

"""
from models import db


class Configuration(db.Model):
    __tablename__ = 'configuration'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    application_name = db.Column(db.String(50),unique=True)

    def __init__(self, application_name):
        self.application_name = application_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()