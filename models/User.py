# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 16:37
@Author : Yu Yuan

"""
from models import db,JsonAble


class User(db.Model, JsonAble):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(512))
    # password_hash = db.Column(db.String(512))

    def __init__(self,username):
        self.username = username

