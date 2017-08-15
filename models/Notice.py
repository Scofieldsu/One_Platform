# -*- coding: utf-8 -*-
"""
@Time : 2017/8/14 16:42
@Author : Yu Yuan

"""
from models import db
from datetime import datetime


class Notice(db.Model):
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    service_name = db.Column(db.String(50))
    action = db.Column(db.String(50))
    time = db.Column(db.DateTime,default=datetime.now)
    link = db.Column(db.String(100))
    checkflag = db.relationship('CheckNotice', backref='notice')


    def __init__(self,user_id,service_name,action,link):
        self.user_id = user_id
        self.service_name = service_name
        self.action = action
        self.link = link

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()