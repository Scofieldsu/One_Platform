# encoding: utf-8
from flaskapi.api import api,api_add
import datetime

@api_add
def test_api(my_dict, my_int, my_str, my_list, my_datetime):
    """
    :description  测试接口
    :param my_dict: dict:字典参数
    :param my_int: int:整型
    :param my_str: str:无默认值
    :param my_list: list:可以省略[]
    :param my_datetime: datetime :时间戳
    :return: code or message
    """

    data1 = my_dict
    data2 = my_int
    data3 = my_str
    data4 = my_list
    data5 = my_datetime
    data6 = datetime.datetime.strptime(my_datetime,'%Y-%m-%d %H:%M:%S')
    result = {
        "my_dict": data1,
        "my_int": data2,
        "my_str": data3,
        "my_list": data4,
        "raw__my_datetime": data5,
        "StrPTime__my_datetime": data6
    }
    return result

@api_add
def hello(name):
    """
    :description welcome to use hello
    :param username: str
    :return:
    """
    return "welcome to use Api-Test,"+name