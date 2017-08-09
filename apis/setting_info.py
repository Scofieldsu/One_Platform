# -*- coding: utf-8 -*-
"""
@Time : 2017/8/9 14:29
@Author : Yu Yuan

"""
from flaskapi.api import api_class
from models.Setting import Setting

@api_class
class SettingApi(object):

    def set_info(self,application_name, gitlab_url, client_id, client_secret, redirect_uri, redirect_server):
        result = dict()
        old_setting = Setting.query.filter_by(application_name=application_name).first()
        if old_setting:
            old_setting.gitlab_url = gitlab_url
            old_setting.client_id = client_id
            old_setting.client_secret = client_secret
            old_setting.redirect_uri = redirect_uri
            old_setting.redirect_server = redirect_server
            old_setting.save()
            result["msg"] = "success"
        else:
            setting = Setting(application_name, gitlab_url, client_id, client_secret, redirect_uri, redirect_server)
            setting.save()
            result["msg"] = "success"
        return result

    def get_info(self,application_name):
        result = dict()
        setting = Setting.query.filter_by(application_name=application_name).first()
        if setting:
            result["application_name"] = setting.application_name or ''
            result["gitlab_url"] = setting.gitlab_url or ''
            result["client_id"] = setting.client_id or ''
            result["client_secret"] = setting.client_secret or ''
            result["redirect_uri"] = setting.redirect_uri or ''
            result["redirect_server"] = setting.redirect_server or ''
            result["msg"] = "success"
        else:
            result["msg"] = "cann't find application"
        return result