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

## 授权模式 （授权码模式：authorization_code；简化模式：implicit；密码模式：password；客户端模式：client_credentials）
GRANT_TYPE = 'authorization_code'
## 回调
CALLBACK = '/login/gitlab'
## 请求access_token
POST_TOKEN_URL =  '/oauth/token'
## 请求gitlab api
GITLAB_API_URL =  '/api/v4/'
## 登录后路径
LOGIN_URL = '/#/yours/notices'
## 默认注册密码
PWD = 'e10adc3949ba59abbe56e057f20f883e'

#　服务动作
ACTION = {
    "add": "发布",
    "update": "更新",
    "delete": "删除"
}


