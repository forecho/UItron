# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app import App
import sys

# python3 test.py https://movie.douban.com/review/8459684/
# or
# python3 test.py 8459684

arg = sys.argv
key = arg[1]

try:
    url = "https://movie.douban.com/review/%d/" % int(key)
except ValueError:
    url = key
crawler = App(url)
print(crawler.send())
