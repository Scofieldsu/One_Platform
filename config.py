# encoding: utf-8
import os

# DEBUG = os.getenv('DEBUG', 'false').lower() == "true"
HERE = os.path.abspath(os.path.dirname(__file__))


# ali-app-settings
AppCODE = '6f5adccc90ff4bd1a249a753dd27d2ea'

# Exchange_rate settings
RATE_HOST =  'http://ali-waihui.showapi.com'
RATE_PATH = '/bank10'
RATE_QUERY = 'bankCode='

# MYSQL
MYSQL_HOST = os.getenv('MYSQL_HOST', '192.168.1.230')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'yuyuan')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'tools')

DEBUG = True

if DEBUG:
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "yuyuan"
    MYSQL_DATABASE = "tools"


def db_uri():
    return 'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?charset=utf8mb4'.format(
        host=MYSQL_HOST, port=MYSQL_PORT, username=MYSQL_USERNAME, password=MYSQL_PASSWORD, dbname=MYSQL_DATABASE)


# database_uri
SQLALCHEMY_DATABASE_URI = db_uri()
SQLALCHEMY_TRACK_MODIFICATIONS = False

# secret_key
SECRET_KEY = 'Bd\x97<q\xfdD\xc9\x85]\xa4\x92\xa3\x9f\x101e\x95\xf1\xf4;\xeem\x8f'






