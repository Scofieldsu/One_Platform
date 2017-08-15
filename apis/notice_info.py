# -*- coding: utf-8 -*-
"""
@Time : 2017/8/14 17:11
@Author : Yu Yuan

"""
import copy
from flaskapi.api import api_class
from models.Notice import Notice
from models.CheckNotice import CheckNotice
from models.User import User


@api_class
class NoticeApi(object):

    def get_notice_list(self,user_id):
        result = list()
        notices = Notice.query.all()
        notices_copy = copy.deepcopy(notices)
        check_notices = CheckNotice.query.filter_by(user_id=user_id).all()
        if notices:
            for x in range(len(notices_copy)):
                if check_notices:
                    for check_notice in check_notices:
                        if check_notice.notice_id == notices_copy[x].id:
                            notices.remove(notices[x])
                        else:
                            result_item = dict()
                            result_item["id"] = notices_copy[x].id
                            result_item["user_name"] = User.query.filter_by(id=notices_copy[x].user_id).first().username
                            result_item["action"] = notices_copy[x].action
                            result_item["service_name"] = notices_copy[x].service_name
                            result_item["time"] = notices_copy[x].time
                            result.append(result_item)
                else:
                    result_item = dict()
                    result_item["id"] = notices_copy[x].id
                    result_item["user_name"] = User.query.filter_by(id=notices_copy[x].user_id).first().username
                    result_item["action"] = notices_copy[x].action
                    result_item["service_name"] = notices_copy[x].service_name
                    result_item["time"] = notices_copy[x].time
                    result.append(result_item)
        return result

    def check_notice(self,user_id,notice_id):
        notice = CheckNotice(user_id,notice_id)
        notice.save()
        result = dict()
        result["msg"] = "success"
        return result
