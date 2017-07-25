# -*- coding: utf-8 -*-
"""
@Time : 2017/7/25 14:46
@Author : Yu Yuan

"""
from models.Service import Service
from models.User import User
from flaskapi.api import api_class


@api_class
class Collections(object):

    def star_on_service(self,user_id,service_id):
        """
        :description 收藏服务
        :param user_id: int:用户ID
        :param service_id: int:服务ID
        :return: msg
        """
        result = dict()
        user = User.query.filter_by(id=user_id).first()
        star_service = Service.query.filter_by(id=service_id).first()
        if not user:
            result["msg"] = "user id error"
            return result
        if not star_service:
            result["msg"] = "service id error"
            return result
        if user and star_service:
            try:
                if star_service in user.collect:
                    result["msg"] = "you have stared on this service before!"
                else:
                    user.collect.append(star_service)
                    user.save()
                    result["msg"] = "success"
            except:
                result["msg"] = "star on append error"
            return result

    def star_off_service(self,user_id,service_id):
        """
        :description  取消收藏服务
        :param user_id: int:用户ID
        :param service_id: int:服务ID
        :return: msg
        """
        result = dict()
        user = User.query.filter_by(id=user_id).first()
        star_service = Service.query.filter_by(id=service_id).first()
        if not user:
            result["msg"] = "user id error"
            return result
        if not star_service:
            result["msg"] = "service id error"
            return result
        if user and star_service:
            try:
                if star_service not in user.collect:
                    result["msg"] = "you do not star on this service!"
                else:
                    user.collect.remove(star_service)
                    user.save()
                    result["msg"] = "success"
            except:
                result["msg"] = "star off remove error"
            return result

    def get_collect_service_list(self,user_id):
        """
        :description 获取该用户收藏服务列表
        :param user_id: int:用户ID
        :return: list
        """
        result = list()
        user = User.query.filter_by(id=user_id).first()
        service_list = user.collect.all()
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
                result_item["change_time"] = service.change_time or ""
                result.append(result_item)
        return result
