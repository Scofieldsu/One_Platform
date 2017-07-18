# -*- coding: utf-8 -*-
"""
@Time : 2017/7/14 11:13
@Author : Yu Yuan

"""

import pytest
from flaskapi.utils.api_tools import trans_str_to_dict, dict_move_key, compose_api_info
from jsonrpc.backend.flask import api

@pytest.fixture
@api.dispatcher.add_method
def show_doc(a=1, b='b'):
    """
    :description test
    :param a:int:int_param
    :param b:str
    :return: test
    """
    return show_doc.__doc__


def test_trans_str_to_dict():
    trans_dict = {
        "description": "test",
        "return": "test",
        "param_explain": {"a":"int_param"},
        "a": "int",
        "b": "str"
    }
    flag = not cmp(trans_str_to_dict(show_doc()), trans_dict)
    assert  flag


def test_dict_move_key():
    b_dict = {
        "b_one": "one",
        "b_two": "two",
    }
    a_dict = {
        "a": "aa",
        "b": b_dict
    }
    c = {
        "a": "aa",
        "b_one": "one",
        "b": {
            "b_two": "two"
        }
    }
    d = dict_move_key(a_dict,b_dict,"b_one")
    flag = not cmp(d, c)
    assert flag



def test_compose_api_info():
    result = compose_api_info("show_doc", api.dispatcher.method_map)
    my_result = {
        "name": "show_doc",
        "description": "test",
        "return": "test",
        "param_explain": {"a": "int_param"},
        "params": {
            "a": "int",
            "b": "str"
        }
    }
    flag = not cmp(result, my_result)
    assert flag
