import requests
import hashlib
import urllib.parse
import random
import json
import init

def translate(string,fr_lang = 'en',to_lang = 'zh'):
    # 所需的参数
    url = 'https://api.fanyi.baidu.com/api/trans/vip/translate'
    
    appid = init.app_info.appid
    secretKey = init.app_info.seckey
    #print(appid,secretKey)
    fromLang = fr_lang
    toLang = to_lang
    salt = random.randint(32768, 65536)
    q = string
    # 拼接字符串后进行MD5加密，hexdigest十六进制，digest二进制
    sign = appid + q + str(salt) + secretKey
    # 字符串应该进行 utf-8 编码再加密
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
    req_URL = f'https://api.fanyi.baidu.com/api/trans/vip/translate?q={urllib.parse.quote(q)}' \
    f'&from={fromLang}&to={toLang}&appid={appid}&salt={salt}&sign={sign}'

    # 请求和异常处理
    try:
        response = requests.get(req_URL)
    except Exception as e:
        print(e)
    else:
        res_dict = json.loads(response.text)
        try:
            return res_dict['trans_result'][0]['dst']
            #print(res_dict['trans_result'][0]['dst'])
        except Exception as e:
            print(f'{e}\n{res_dict}')

if __name__ == "__main__":
    print(translate("hello",'en','zh'))