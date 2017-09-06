# -*- coding: utf-8 -*-
"""
@Time : 2017/9/6 13:42
@Author : Yu Yuan

"""

from models import db
from datetime import datetime


class Publicinfo(db.Model):
    __tablename__ = 'public_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime,default=datetime.now)
    update_user = db.Column(db.Integer)
    update_time = db.Column(db.DateTime,default=datetime.now)


    def __init__(self,user_id,title,content):
        self.user_id = user_id
        self.title = title
        self.update_user = user_id
        self.content = content

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()