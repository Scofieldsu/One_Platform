# -*- coding: utf-8 -*-
"""
@Time : 2017/7/18 14:08
@Author : Yu Yuan

"""

import glob
import os

basedir = os.path.abspath(os.path.dirname(__file__))


def register_controller(app):
    """自动查找Controller下的蓝图控制器 自动注册"""

    mod_path = os.path.dirname(__file__)
    pys = glob.glob(os.path.join(mod_path, '*.py'))
    blueprint_dict = list()
    map(lambda x: blueprint_dict.append(x.split(os.sep)[-1:][0][:-3]), pys)
    for x in blueprint_dict:
        if x[-2:] != "__":
            mod = __import__("controller." + x, fromlist=[x])
            mod_attr = getattr(mod, x)
            app.register_blueprint(mod_attr)