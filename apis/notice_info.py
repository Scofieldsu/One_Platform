# -*- coding: utf-8 -*-
"""
@Time : 2017/8/14 17:11
@Author : Yu Yuan

"""
import datetime
from flaskapi.api import api_class
from models.Notice import Notice
from models.CheckNotice import CheckNotice
from models.User import User


@api_class
class NoticeApi(object):

    def get_notice_list(self,user_id):
        """
        :description 获取通知信息列表
        :param user_id: int:用户ID
        :return: list
        """
        result = list()
        # 只获取7天内的通知
        filters = {
            Notice.time >  (datetime.datetime.now()-datetime.timedelta(days=7))
        }
        notices = Notice.query.filter(*filters).all()
        check_notices = CheckNotice.query.filter_by(user_id=user_id).all()
        if notices:
            if check_notices:
                for check_notice in check_notices:
                    for x in notices:
                        if check_notice.notice_id == x.id:
                            notices.remove(x)
                for x in range(len(notices)):
                    result_item = dict()
                    result_item["id"] = notices[x].id
                    u = User.query.filter_by(id=notices[x].user_id).first()
                    if u:
                        result_item["user_name"] = u.username
                    else:
                        result_item["user_name"] = ""
                    result_item["action"] = notices[x].action
                    result_item["service_name"] = notices[x].service_name
                    result_item["time"] = notices[x].time
                    result_item["link"] = notices[x].link
                    result.append(result_item)
            else:
                for notice_item in notices:
                    result_item = dict()
                    result_item["id"] = notice_item.id
                    u = User.query.filter_by(id=notice_item.user_id).first()
                    if u:
                        result_item["user_name"] = u.username
                    else:
                        result_item["user_name"] = ""
                    result_item["action"] = notice_item.action
                    result_item["service_name"] = notice_item.service_name
                    result_item["time"] = notice_item.time
                    result_item["link"] = notice_item.link
                    result.append(result_item)
        return result

    def check_notice(self,user_id,notice_id):
        """
        :description  关闭某个通知消息
        :param user_id: int:用户ID
        :param notice_id: int:通知ID
        :return: msg
        """
        notice = CheckNotice(user_id,notice_id)
        notice.save()
        result = dict()
        result["msg"] = "success"
        return result
