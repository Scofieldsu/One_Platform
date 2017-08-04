# encoding: utf-8
import os

DEBUG = os.getenv('DEBUG', 'false').lower() == "true"
HERE = os.path.abspath(os.path.dirname(__file__))


# ali-app-settings
AppCODE = '6f5adccc90ff4bd1a249a753dd27d2ea'

# Exchange_rate settings
RATE_HOST =  'http://ali-waihui.showapi.com'
RATE_PATH = '/bank10'
RATE_QUERY = 'bankCode='

# MYSQL
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'yuyuan')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'tools')



def db_uri():
    return 'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4'.format(
        host=MYSQL_HOST, port=MYSQL_PORT, username=MYSQL_USERNAME, password=MYSQL_PASSWORD, dbname=MYSQL_DATABASE)


# database_uri
SQLALCHEMY_DATABASE_URI = db_uri()
SQLALCHEMY_TRACK_MODIFICATIONS = False

# secret_key
SECRET_KEY = 'Bd\x97<q\xfdD\xc9\x85]\xa4\x92\xa3\x9f\x101e\x95\xf1\xf4;\xeem\x8f'

# gitlab oauth认证信息

## 回调服务
BASE_SERVICE = 'http://192.168.1.230:5050'
## gitlab地址
BASE_GITLAB = 'http://192.168.5.10'
## application ID
CLIENT_ID = 'a164506151fbd065a97d3cd9654ee0e37f80ffe81616a8311c320022a097e2c3'
## application SECRET
CLIENT_SECRET = '702b9408eca977655b7b7f1404143fc98efc7e28ebf70834467e3cf8b1ef55e6'
## 授权模式 （授权码模式：authorization_code；简化模式：implicit；密码模式：password；客户端模式：client_credentials）
GRANT_TYPE = 'authorization_code'
## 回调
CALLBACK = '/login/gitlab'
## 回调链接
REDIRECT_URI = BASE_SERVICE+CALLBACK
## 请求access_token
POST_TOKEN_URL = BASE_GITLAB + '/oauth/token'
## 请求gitlab api
GITLAB_API_URL = BASE_GITLAB + '/api/v4/'
## 登录后路径
LOGIN_URL = BASE_SERVICE + '/#/yours/notices'
## 默认注册密码
PWD = 'e10adc3949ba59abbe56e057f20f883e'





