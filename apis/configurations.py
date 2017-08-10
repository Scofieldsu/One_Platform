# -*- coding: utf-8 -*-
"""
@Time : 2017/8/10 10:37
@Author : Yu Yuan

"""
from flaskapi.api import api_class
from models.Configuration import Configuration

@api_class
class ConfigurationApi(object):

    def set_application(self,application_name):
        """
        :description 设置当前gitlab应用
        :param application_name: str:gitlab应用名称
        :return:
        """
        result = dict()
        configurations = Configuration.query.all()
        if not configurations:
            configuration = Configuration(application_name)
            configuration.save()
            result["msg"] = "success"
        elif  len(configurations) == 1:
            configurations[0].application_name = application_name
            configurations[0].save()
            result["msg"] = "success"
        else:
            result["msg"] = "Configuration error"
        return result