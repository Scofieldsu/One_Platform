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

# gitlab
BASE_SERVICE = 'http://192.168.1.230:5050'
BASE_GITLAB = 'http://10.46.59.55'
CLIENT_ID = '7a399849bf58eb8f983728b6fdd543c453e7c792d0d10b2b87ba88a7da6da3d1'
CLIENT_SECRET = 'd4f5dcb964c9d2fc9219fe98347502d9798268e70fd7b4209a3c18b4e8d8c49a'
GRANT_TYPE = 'authorization_code'
CALLBACK = '/login/gitlab'
REDIRECT_URI = BASE_SERVICE+CALLBACK
POST_TOKEN_URL = BASE_GITLAB + '/oauth/token'
GITLAB_API_URL = BASE_GITLAB + '/api/v4/'
LOGIN_URL = BASE_SERVICE + '/#/yours/notices'
PWD = 'e10adc3949ba59abbe56e057f20f883e'





