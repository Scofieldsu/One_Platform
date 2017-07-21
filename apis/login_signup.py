# -*- coding: utf-8 -*-
"""
@Time : 2017/7/19 17:23
@Author : Yu Yuan

"""
import hashlib
from flaskapi.api import api_add
from models.User import User
from models import db


# md5密码
def  hash_pwd(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


@api_add
def sign_up(username,email,password):
    """
    :description 注册
    :param username: str:姓名
    :param email: str:邮箱
    :param password: str:密码（MD5）
    :return: msg
    """
    result = dict()
    query_user = User.query.filter_by(email=email).first()
    if query_user:
        result["msg"] = "The email has been registered"
    else :
        sign_up_user = User(username, email, password)
        sign_up_user.save()
        result["msg"] = "success"
    return result


@api_add
def sign_in(email,password):
    """
    :description 登录
    :param email: str:邮箱
    :param password: str:密码（MD5）
    :return: msg
    """
    sign_in_user = User.query.filter_by(email=email).first()
    result = dict()
    if sign_in_user:
        pwd = sign_in_user.password_hash
        if pwd == password or pwd == hash_pwd(password):
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


@api_add
def change_pwd(user_id,old_pwd,new_pwd):
    """
    :description 修改密码
    :param user_id: int:用户ID
    :param old_pwd: str:旧密码
    :param new_pwd: str:新密码
    :return: msg
    """
    result = dict()
    change_pwd_user = User.query.filter_by(id=user_id).first()
    if not user_id or not change_pwd_user :
        result["msg"] = "user dose not exist!"
    elif old_pwd != change_pwd_user.password_hash:
        result["msg"] = "The old password is wrong!"
    else:
        change_pwd_user.password_hash = new_pwd
        db.session.add(change_pwd_user)
        db.session.commit()
        result["msg"] = "success"
    return result
