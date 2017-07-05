# encoding: utf-8

import urllib, urllib2, sys, json
from flaskapi.api import api_add,api
from config import RATE_HOST,RATE_PATH,RATE_QUERY,AppCODE


examp_result = {"showapi_res_code":0,
                "showapi_res_error":"",
                "showapi_res_body":
                    {"time":"23:11:59",
                     "ret_code":0,
                     "name":"ICBC",
                     "codeList":
                         [{"hui_in":"6.0144",
                           "chao_out":"6.0566",
                           "chao_in":"5.8769",
                           "hui_out":"6.0566",
                           "name":"日元",
                           "zhesuan":"",
                           "mid_price":"--",
                           "code":"JPY"
                           },
                          {"hui_in":"490.4000","chao_out":"493.8500","chao_in":"479.1900","hui_out":"493.8500","name":"新加坡元","zhesuan":"","mid_price":"--","code":"SGD"},{"hui_in":"86.8300","chao_out":"87.1800","chao_in":"86.2600","hui_out":"87.1800","name":"港币","zhesuan":"","mid_price":"--","code":"HKD"},{"hui_in":"84.3000","chao_out":"84.6400","chao_in":"83.7500","hui_out":"84.6400","name":"澳门元","zhesuan":"","mid_price":"--","code":"MOP"},{"hui_in":"520.8600","chao_out":"524.5100","chao_in":"508.9500","hui_out":"524.5100","name":"加拿大元","zhesuan":"","mid_price":"--","code":"CAD"},{"hui_in":"52.1400","chao_out":"52.5100","chao_in":"50.1100","hui_out":"52.5100","name":"南非兰特","zhesuan":"","mid_price":"--","code":"ZAR"},{"hui_in":"493.9500","chao_out":"497.4200","chao_in":"482.6600","hui_out":"497.4200","name":"新西兰元","zhesuan":"","mid_price":"--","code":"NZD"},{"hui_in":"519.6400","chao_out":"523.2900","chao_in":"507.7600","hui_out":"523.2900","name":"澳大利亚元","zhesuan":"","mid_price":"--","code":"AUD"},{"hui_in":"879.5500","chao_out":"885.7200","chao_in":"859.4400","hui_out":"885.7200","name":"英镑","zhesuan":"","mid_price":"--","code":"GBP"},{"hui_in":"103.9800","chao_out":"104.7100","chao_in":"101.6000","hui_out":"104.7100","name":"丹麦克朗","zhesuan":"","mid_price":"--","code":"DKK"},{"hui_in":"80.6500","chao_out":"81.2200","chao_in":"78.8100","hui_out":"81.2200","name":"挪威克朗","zhesuan":"","mid_price":"--","code":"NOK"},{"hui_in":"79.7600","chao_out":"80.3200","chao_in":"77.9300","hui_out":"80.3200","name":"瑞典克朗","zhesuan":"","mid_price":"--","code":"SEK"},{"hui_in":"157.6400","chao_out":"158.7400","chao_in":"--","hui_out":"158.7400","name":"林吉特","zhesuan":"","mid_price":"--","code":"MYR"},{"hui_in":"198.6500","chao_out":"218.4300","chao_in":"198.6500","hui_out":"218.4300","name":"巴西里亚尔","zhesuan":"","mid_price":"--","code":"BRL"},{"hui_in":"707.2400","chao_out":"712.2100","chao_in":"691.0700","hui_out":"712.2100","name":"瑞士法郎","zhesuan":"","mid_price":"--","code":"CHF"},{"hui_in":"773.2200","chao_out":"778.6500","chao_in":"755.5400","hui_out":"778.6500","name":"欧元","zhesuan":"","mid_price":"--","code":"EUR"},{"hui_in":"11.4600","chao_out":"11.5400","chao_in":"11.1700","hui_out":"11.5400","name":"卢布","zhesuan":"","mid_price":"--","code":"RUB"},{"hui_in":"13.0530","chao_out":"13.4820","chao_in":"13.0530","hui_out":"13.4820","name":"菲律宾比索","zhesuan":"","mid_price":"--","code":"PHP"},{"hui_in":"677.7200","chao_out":"680.4400","chao_in":"673.3100","hui_out":"680.4400","name":"美元","zhesuan":"","mid_price":"--","code":"USD"},{"hui_in":"19.9100","chao_out":"20.0500","chao_in":"19.4100","hui_out":"20.0500","name":"泰国铢","zhesuan":"","mid_price":"--","code":"THB"},{"hui_in":"--","chao_out":"--","chao_in":"--","hui_out":"--","name":"","zhesuan":"","mid_price":"--","code":"RMB"},{"hui_in":"--","chao_out":"0.5956","chao_in":"0.5779","hui_out":"0.5956","name":"韩国元","zhesuan":"","mid_price":"--","code":"KRW"},{"hui_in":"21.6700","chao_out":"23.2500","chao_in":"21.6700","hui_out":"23.2500","name":"新台币","zhesuan":"","mid_price":"--","code":"TWD"}],"day":"2017-06-29","listSize":23}}


@api_add
def get_rate(bank):
    # url = RATE_HOST + RATE_PATH + '?' + RATE_QUERY+bank
    # request = urllib2.Request(url)
    # request.add_header('Authorization', 'APPCODE ' + AppCODE)
    # response = urllib2.urlopen(request)
    # content = json.loads(response.read())
    # if (content):
    #     print(content)
    return examp_result