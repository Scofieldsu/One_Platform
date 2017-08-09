# -*- coding: utf-8 -*-
"""
@Time : 2017/7/19 17:23
@Author : Yu Yuan

"""
import hashlib
from flaskapi.api import api_class
from models.User import User


# md5密码
def  hash_pwd(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


@api_class
class UserApi(object):

    def sign_up(self,username, email, password):
        """
        :description 注册
        :param username: str:姓名
        :param email: str:邮箱
        :param password: str:密码（MD5）
        :return: msg
        """
        result = dict()
        query_user = User.query.filter_by(email=email).first()
        if query_user and not query_user.active:
            result["msg"] = "The email has been registered but not active"
        elif query_user and query_user.active:
            result["msg"] = "The email has been registered"
        else:
            sign_up_user = User(username, email, password)
            sign_up_user.save()
            result["msg"] = "success"
        return result

    def sign_in(self,email, password):
        """
        :description 登录
        :param email: str:邮箱
        :param password: str:密码（MD5）
        :return: msg
        """
        sign_in_user = User.query.filter_by(email=email).first()
        result = dict()
        if sign_in_user and sign_in_user.active:
            pwd = sign_in_user.password_hash
            if pwd == password or pwd == hash_pwd(password):
                user_id = sign_in_user.id
                user_name = sign_in_user.username
                result["user_id"] = user_id
                result["user_name"] = user_name
                result["msg"] = "success"
            else:
                result["msg"] = "password error"
        elif sign_in_user and not sign_in_user.active:
            result["msg"] = "user is not active"
        else:
            result["msg"] = "email error"
        return result

    def change_pwd(self,user_id, old_pwd, new_pwd):
        """
        :description 修改密码
        :param user_id: int:用户ID
        :param old_pwd: str:旧密码
        :param new_pwd: str:新密码
        :return: msg
        """
        result = dict()
        change_pwd_user = User.query.filter_by(id=user_id).first()
        if not user_id or not change_pwd_user:
            result["msg"] = "user dose not exist!"
        elif old_pwd != change_pwd_user.password_hash:
            result["msg"] = "The old password is wrong!"
        else:
            change_pwd_user.password_hash = new_pwd
            change_pwd_user.save()
            result["msg"] = "success"
        return result

    def get_user_list(self,user_id):
        """
        :description 获取用户列表
        :param user_id: int:用户ID
        :return: list
        """
        result = list()
        user_list = User.query.all()
        if user_list:
            for user in user_list:
                result_item = dict()
                result_item["id"] = user.id
                result_item["username"] = user.username
                result_item["email"] = user.email
                if user.active:
                    result_item["active"] = 1
                else:
                    result_item["active"] = 0
                result.append(result_item)
        return result

    def set_user_enable(self,user_id, op_user_id):
        """
        :description 设置用户有效
        :param user_id: int:用户ID
        :param op_user_id:int:被设置的用户ID
        :return:msg
        """
        result = dict()
        op_user = User.query.filter_by(id=op_user_id).first()
        if op_user:
            if op_user.active:
                result["msg"] = "User has been Enable!"
            else:
                op_user.enable()
                result["msg"] = "success"
        else:
            result["msg"] = "user id  error!"
        return result

    def set_user_disable(self,user_id, op_user_id):
        """
        :description 设置用户无效
        :param user_id: int:用户ID
        :param op_user_id:int:被设置的用户ID
        :return:msg
        """
        result = dict()
        op_user = User.query.filter_by(id=op_user_id).first()
        if op_user:
            if not op_user.active:
                result["msg"] = "User has been Disable!"
            else:
                op_user.disable()
                result["msg"] = "success"
        else:
            result["msg"] = "user id  error!"
        return result

    def get_access_token(self,user_id):
        """
        :description 获取用户gitlab的access_token
        :param user_id: int: 用户ID
        :return: msg
        """
        result = dict()
        user = User.query.filter_by(id=user_id).first()
        if user :
            result["access_token"] = user.access_token or ''
            result["msg"] = 'success'
        else:
            result["msg"] = "cann't find user"
        return result