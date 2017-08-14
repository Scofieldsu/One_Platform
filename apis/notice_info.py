# -*- coding: utf-8 -*-
"""
@Time : 2017/8/14 17:11
@Author : Yu Yuan

"""
from flaskapi.api import api_class
from models.Notice import Notice
from models.CheckNotice import CheckNotice
from models.User import User


@api_class
class NoticeApi(object):

    def get_notice_list(self,user_id):
        result = list()
        notices = Notice.query.all()
        check_notices = CheckNotice.query.filter_by(user_id=user_id).all()
        if notices:
            for notice in notices:
                if check_notices:
                    for check_notice in check_notices:
                        if check_notice.notice_id == notice.id:
                            notices.remove(notice)
                        else:
                            result_item = dict()
                            result_item["id"] = notice.id
                            result_item["user_name"] = User.query.filter_by(id=notice.user_id).first().username
                            result_item["action"] = notice.action
                            result_item["service_name"] = notice.service_name
                            result.append(result_item)
                else:
                    result_item = dict()
                    result_item["id"] = notice.id
                    result_item["user_name"] = User.query.filter_by(id=notice.user_id).first().username
                    result_item["action"] = notice.action
                    result_item["service_name"] = notice.service_name
                    result.append(result_item)
        return result

