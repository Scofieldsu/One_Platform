# -*- coding: utf-8 -*-
"""
@Time : 2017/7/21 14:48
@Author : Yu Yuan

"""
from flaskapi.api import api_add
from models import db
from models.User import User
from models.Service import Service


@api_add
def add_service(user_id,service_name,link,tag,shortcut,desc,notice):
    """
    :description 发布服务
    :param user_id:int:用户ID
    :param service_name:str:服务名称
    :param link:str:服务链接
    :param tag:str:标签
    :param shortcut:str:短称
    :param desc:str:简介
    :param notice:int:是否通知
    :return:msg
    """
    service_by_name = Service.query.filter_by(service_name=service_name).first()
    service_by_link = Service.query.filter_by(link=link).first()
    result = dict()
    if service_by_name:
        result["msg"] = "服务名称已存在！"
    elif service_by_link:
        result["msg"] = "链接已存在！"
    else:
        service_by_add = Service(user_id,service_name,link,shortcut,notice,tag,desc)
        service_by_add.save()
        result["msg"] = "success"
    return result


@api_add
def get_service_list(user_id):
    result = list()
    service_list = Service.query.all()
    if service_list:
        for service in service_list:
            result_item = dict()
            result_item["name"] = service.service_name
            result_item["link"] = service.link
            result_item["shortcut"] = service.shortcut or ""
            result_item["tag"] = service.tag or ""
            result_item["publish_time"] = service.publish_time or ""
            result_item["publish_user"] = service.users.username or ""
            result_item["change_time"] = service.change_time or ""
            result.append(result_item)
    return result

