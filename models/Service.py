# -*- coding: utf-8 -*-
"""
@Time : 2017/7/19 10:42
@Author : Yu Yuan

"""
from models import db
from datetime import datetime


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_name = db.Column(db.String(50),unique=True)
    link = db.Column(db.String(100),unique=True)
    tag = db.Column(db.String(50))
    description = db.Column(db.String(200))
    publish_time = db.Column(db.DateTime,default=datetime.utcnow)
    change_time = db.Column(db.DateTime)
    publish_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,service_name,link,tag,description,change_time):
        self.service_name = service_name
        self.link = link
        self.tag = tag
        self.description = description
        self.change_time = change_time
