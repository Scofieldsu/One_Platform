# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 16:37
@Author : Yu Yuan

"""
from models import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password_hash = db.Column(db.String(120))
    services = db.relationship('Service', backref='users')
    messages = db.relationship('Message', backref='users')


    def __init__(self,username,email,password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def save(self):
        db.session.add(self)
        db.session.commit()

