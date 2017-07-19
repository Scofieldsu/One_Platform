# -*- coding: utf-8 -*-
"""
@Time : 2017/7/19 17:23
@Author : Yu Yuan

"""
import hashlib
from flaskapi.api import api_add
from models.User import User
from models import db



@api_add
def sign_up(username,email,password):
    sign_up_user = User(username,email,password)
    db.session.add(sign_up_user)
    db.session.commit()
    result = dict()
    result["msg"] = "success"
    return result


@api_add
def sign_in(email,password):
    sign_in_user = User.query.filter_by(email=email).first()
    result = dict()
    if sign_in_user:
        md = hashlib.md5()
        md.update(password)
        pwd = sign_in_user.password_hash
        if pwd == password or pwd == md.hexdigest():
            user_id = sign_in_user.id
            user_name = sign_in_user.username
            result["user_id"] = user_id
            result["user_name"] = user_name
            result["msg"] = "success"
        else:
            result["msg"] = "password error"
    else:
        result["msg"] = "email error"
    return result
