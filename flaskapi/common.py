# encoding: utf-8
import sys
from flaskapi.api.base_api import *
from flaskapi.utils.api_tools import compose_api_info



@api_add
def get_all_api(*args, **kwargs):
    """
    :description 获取接口信息
    :param args:str
    :param kwargs:str
    :return: 所有接口信息
    """
    # 从method_map获取所有接口方法，重组数格式
    _name = sys._getframe().f_code.co_name
    api_dict = api.dispatcher.method_map
    api_name_list = api_dict.keys()
    result = {}
    for i in api_name_list:
        item = compose_api_info(i, api_dict)
        result[i] = item
    result.pop(_name)
    if "hello" in result:
        result.pop("hello")
    return result


# get_all_api返回的数据格式
def get_all_api_temp(*args, **kwargs):
    result = {'login': {'name': 'login', 'description': '登录接口', 'return': '返回信息', 'param_explain': {},  'params': {'login_name': 'str', "password": "str"}},
              'logout': {'name': 'logout', 'description': '退出', 'return': '返回信息',  'param_explain': {}, 'params': {"name": "str", "pwd": "str"}}}
    return result