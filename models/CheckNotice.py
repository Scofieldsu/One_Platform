# -*- coding: utf-8 -*-
"""
@Time : 2017/8/14 16:42
@Author : Yu Yuan

"""
from models import db
from datetime import datetime


class CheckNotice(db.Model):
    __tablename__ = 'check_notice'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    notice_id = db.Column(db.Integer, db.ForeignKey('notice.id'))

    def __init__(self, user_id, notice_id):
        self.user_id = user_id
        self.notice_id = notice_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
