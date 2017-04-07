# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app import App
import sys

# python3 test.py https://movie.douban.com/review/8459684/
arg = sys.argv
crawler = App(arg[1])
print(crawler.send())
