# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import requests
import hashlib
import json
from common.helper import Helper


class Translate:
    def __init__(self):
        pass

    @staticmethod
    def baidu(text, to_lang='en'):
        baidu = Helper.config('baidu')
        salt = random.randint(32768, 65536)
        sign = str(baidu['appid']) + text + str(salt) + baidu['secretKey']
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()

        payload = {'appid': baidu['appid'], 'q': text, 'from': 'auto', 'to': to_lang, 'salt': salt, 'sign': sign}
        # 捕捉异常
        try:
            r = requests.post(baidu['link'], data=payload)
            parsed_json = json.loads(r.content.decode('utf-8'))
            dst = parsed_json['trans_result'][0]['dst']
        except Exception:
            return ''
        return dst
