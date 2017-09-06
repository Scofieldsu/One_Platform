# -*- coding: utf-8 -*-
"""
@Time : 2017/9/6 14:04
@Author : Yu Yuan

"""

from datetime import datetime
from flaskapi.api import api_class
from models.Publlicinfo import Publicinfo
from models.User import User
from models import db


@api_class
class PublicInfoApi(object):

    def add_public_info(self,user_id,title,content):
        """
        :description 发布公告接口
        :param user_id: int:用户ID
        :param title: string:公告标题
        :param content: string:公告内容
        :return: msg
        """
        result = dict()
        public_info = Publicinfo(user_id,title,content)
        public_info.save()
        result['msg'] = 'success'
        return result

    def get_public_info_list(self,user_id):
        """
        :description  获取公告列表
        :param user_id: int: 用户ID
        :return: list
        """
        result = list()
        public_info_list = Publicinfo.query.order_by(db.desc(Publicinfo.update_time)).all()
        if public_info_list:
            for public_info in public_info_list:
                result_item = dict()
                result_item['id'] = public_info.id
                result_item['title'] = public_info.title
                result_item['content'] = public_info.content
                result_item['summary'] = result_item['content'][:100]
                result_item['time'] = public_info.create_time
                result_item['update_time'] = public_info.update_time
                try:
                    result_item["user"] = User.query.filter_by(id=public_info.user_id).first().username
                except:
                    result_item["user"] = ""
                try:
                    result_item["update_user"] = User.query.filter_by(id=public_info.update_user).first().username
                except:
                    result_item["update_user"] = ""
                result.append(result_item)
        return result

    def get_public_info(self,user_id,pubinfo_id):
        """
        :description 获取单个公告
        :param user_id: int:用户ID
        :param pubinfo_id: int:公告ID
        :return: dict
        """
        result = dict()
        public_info = Publicinfo.query.filter_by(id=pubinfo_id).first()
        if public_info:
            result['id'] = public_info.id
            result['title'] = public_info.title
            result['content'] = public_info.content
        return result

    def update_public_info(self,user_id,pubinfo_id,title,content):
        """
        :description 更新公告
        :param user_id:int:用户ID
        :param pubinfo_id:int:公告ID
        :param title:str:公告标题
        :param content:str:公告内容
        :return: msg
        """
        result = dict()
        public_info = Publicinfo.query.filter_by(id=pubinfo_id).first()
        if public_info:
            try:
                public_info.title = title
                public_info.content = content
                public_info.update_user = user_id
                public_info.update_time = datetime.now()
                public_info.save()
                result["msg"] = "success"
            except:
                result["msg"] = "update public info failed"
        else:
            result["msg"] = "pubinfo id error"
        return result

    def delete_public_info(self, user_id, pubinfo_id):
        """
        :description 删除公告
        :param user_id: int:用户ID
        :param pubinfo_id: int:公告ID
        :return: msg
        """
        result = dict()
        pubinfo = Publicinfo.query.filter_by(id=pubinfo_id).first()
        if pubinfo:
            pubinfo.delete()
            result['msg'] = 'success'
        else:
            result["msg"] = "pubinfo id error"
        return result
