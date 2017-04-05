# !/usr/bin/env python
# -*- coding: utf-8 -*-
from movie.douban import Douban


class App:
    def __init__(self, base_url):
        self.base_url = base_url

    def crawl(self):
        return Douban.get_post_from_link(self.base_url)
        return


crawler = App('https://movie.douban.com/review/8456179/')
print(crawler.crawl())
