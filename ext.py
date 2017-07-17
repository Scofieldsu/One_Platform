# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 16:22
@Author : Yu Yuan

"""
from datetime import datetime
from sqlalchemy import Column, DateTime
from flask_sqlalchemy import SQLAlchemy, Model


class BaseModel(Model):
    create_at = Column(DateTime, default=datetime.utcnow())

    def to_dict(self):
        columns = self.__table__.columns.keys()
        return {key: getattr(self, key) for key in columns}


db = SQLAlchemy(model_class=BaseModel)