# -*- coding: utf-8 -*-
"""
@Time : 2017/7/24 9:16
@Author : Yu Yuan

"""
from flaskapi.api import api_add
from models.Message import Message


@api_add
def add_message(user_id,content):
    """
    :description 新增留言
    :param user_id: int:用户ID
    :param content: int:留言内容
    :return: msg
    """
    result = dict()
    leave_message = Message(user_id,content)
    leave_message.save()
    result["msg"] = "success"
    return result


@api_add
def get_message_list(user_id):
    """
    :description 获取留言列表
    :param user_id: int :用户ID
    :return: list
    """
    result = list()
    message_list = Message.query.all()
    if message_list:
        for message in message_list:
            result_item = dict()
            result_item["message"] = message.content
            result_item["message_time"] = message.leave_time
            result_item["message_user"] = message.users.username
            result.append(result_item)
    return result