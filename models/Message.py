# -*- coding: utf-8 -*-
"""
@Time : 2017/7/24 9:02
@Author : Yu Yuan

"""
from models import db
from datetime import datetime



class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(500))
    leave_time = db.Column(db.DateTime,default=datetime.now)
    leave_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,user_id,content):
        self.content = content
        self.leave_user = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

