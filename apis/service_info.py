# -*- coding: utf-8 -*-
"""
@Time : 2017/7/21 14:48
@Author : Yu Yuan

"""
from flaskapi.api import api_class
from models.Service import Service
from models.User import User
from datetime import datetime
from models.Notice import Notice
from config import ACTION


@api_class
class ServiceApi(object):

    def add_service(self,user_id, service_name, link, tag, shortcut, desc, notice):
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
            service_by_add = Service(user_id, service_name, link, shortcut, notice, tag, desc)
            service_by_add.save()
            # 更新通知
            if notice:
                action = ACTION["add"]
                add_notice = Notice(user_id,service_name,action)
                add_notice.save()
            result["msg"] = "success"
        return result

    def get_service_list(self,user_id):
        """
        :description 获取所有服务
        :param user_id: int:用户ID
        :return: list
        """
        result = list()
        service_list = Service.query.all()
        if service_list:
            for service in service_list:
                result_item = dict()
                result_item["id"] = service.id
                result_item["name"] = service.service_name
                result_item["link"] = service.link
                result_item["shortcut"] = service.shortcut or ""
                result_item["tag"] = service.tag or ""
                result_item["publish_time"] = service.publish_time or ""
                result_item["publish_user"] = service.users.username or ""
                result_item["count"] = service.visit_count or 0
                try:
                    result_item["update_user"] = User.query.filter_by(id=service.update_user).first().username
                except:
                    result_item["update_user"] = ""
                result_item["change_time"] = service.change_time or ""
                result.append(result_item)
        return result

    def get_service(self,user_id, service_id):
        """
        :description 获取单个服务信息
        :param user_id: int:用户ID
        :param service_id: int :服务ID
        :return:dict
        """
        result = dict()
        service = Service.query.filter_by(id=service_id).first()
        if service:
            result["id"] = service_id
            result["name"] = service.service_name
            result["link"] = service.link
            result["shortcut"] = service.shortcut or ""
            result["tag"] = service.tag or ""
            result["notice"] = service.notice
            result["desc"] = service.description or ""
            result["count"] = service.visit_count or 0
            result["msg"] = "success"
        else:
            result["msg"] = "failed to find service"
        return result

    def delete_service(self,user_id,service_id):
        """
        :description 删除服务
        :param user_id: int:用户ID
        :param service_id: int:服务ID
        :return: msg
        """
        result = dict()
        service = Service.query.filter_by(id=service_id).first()
        if service:
            service.delete()
            # 更新通知
            action = ACTION["delete"]
            add_notice = Notice(user_id, service.service_name, action)
            add_notice.save()
            result["msg"] = "success"
        else:
            result["msg"] = "service id error"
        return result

    def visit_service(self,user_id,service_id):
        """
        :description 访问服务
        :param user_id: int:用户ID
        :param service_id: int:服务ID
        :return: msg
        """
        result = dict()
        service = Service.query.filter_by(id=service_id).first()
        if service:
            service.visit()
            result["msg"] = "success"
        else:
            result["msg"] = "service id error"
        return result

    def update_service(self,user_id,service_id,service_name,link,tag,shortcut,desc,notice):
        """
        :description 更新服务信息
        :param user_id: int:用户ID
        :param service_id: int:服务ID
        :param service_name: str:服务名称
        :param link: str:服务链接
        :param tag: str:服务标签
        :param shortcut:str: 服务短称
        :param desc: str:服务简介
        :param notice: int:服务通知
        :return: msg
        """
        result = dict()
        service = Service.query.filter_by(id=service_id).first()
        if service:
            try:
                service.service_name = service_name
                service.link = link
                service.tag = tag
                service.shortcut = shortcut
                service.description = desc
                service.notice = notice
                service.update_user = user_id
                service.change_time = datetime.now()
                service.save()
                # 更新通知
                action = ACTION["update"]
                add_notice = Notice(user_id, service_name, action,link)
                add_notice.save()
                result["msg"] = "success"
            except:
                result["msg"] = "update service data failed"
        else:
            result["msg"] = "service id error"
        return result

