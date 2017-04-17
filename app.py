# !/usr/bin/env python
# -*- coding: utf-8 -*-
from movie.douban import Douban
from common.helper import Helper
import requests
import json
from requests.auth import HTTPBasicAuth


class App:
    def __init__(self, base_url):
        self.base_url = base_url

    def crawl(self):
        return Douban.get_post(self.base_url)

    def send(self):
        data = self.crawl()
        if data:
            wordpress = Helper.config('wordpress')
            meta_data = {
                'categories': wordpress['categories'],
                'author': wordpress['author'],
                'status': wordpress['status']
            }
            payload = Helper.merge_two_dicts(meta_data, data)
            r = requests.post(wordpress['link'], data=payload, auth=HTTPBasicAuth(wordpress['user'], wordpress['password']))
            if r.status_code < 300:
                return '成功'
            # parsed_json = json.loads(r.content.decode('utf-8'))
            return '失败'
        return '链接不存在'

    def cycle(self):
        pass

# crawler = App('https://movie.douban.com/review/8456179/')
# # data = crawler.crawl()
# print(crawler.send())
