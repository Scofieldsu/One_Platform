# encoding: utf-8
import os

DEBUG = True
HERE = os.path.abspath(os.path.dirname(__file__))


# ali-app-settings
AppCODE = '6f5adccc90ff4bd1a249a753dd27d2ea'

# Exchange_rate settings
RATE_HOST =  'http://ali-waihui.showapi.com'
RATE_PATH = '/bank10'
RATE_QUERY = 'bankCode='

# database_uri
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yuyuan@localhost/tools'
SQLALCHEMY_TRACK_MODIFICATIONS = False


