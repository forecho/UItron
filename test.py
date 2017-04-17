# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app import App
import sys
from bs4 import BeautifulSoup
import requests

# python3 test.py https://movie.douban.com/review/8459684/
# or
# python3 test.py 8459684

# arg = sys.argv
# key = arg[1]
#
# try:
#     url = "https://movie.douban.com/review/%d/" % int(key)
# except ValueError:
#     url = key
# crawler = App(url)
# print(crawler.send())

url = 'https://movie.douban.com/review/best/'

page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
for a in soup.findAll('a', 'title-link'):
    crawler = App(a.get('href'))
    print(crawler.send())