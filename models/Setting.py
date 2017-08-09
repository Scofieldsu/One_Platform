# -*- coding: utf-8 -*-
"""
@Time : 2017/8/9 14:18
@Author : Yu Yuan

"""

from models import db


class Setting(db.Model):
    __tablename__ = 'setting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    application_name = db.Column(db.String(50),unique=True)
    gitlab_url = db.Column(db.String(120))
    client_id = db.Column(db.String(120))
    client_secret = db.Column(db.String(120))
    redirect_uri = db.Column(db.String(120))
    redirect_server = db.Column(db.String(120))

    def __init__(self, application_name, gitlab_url, client_id, client_secret, redirect_uri, redirect_server):
        self.application_name = application_name
        self.gitlab_url = gitlab_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.redirect_server = redirect_server

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()