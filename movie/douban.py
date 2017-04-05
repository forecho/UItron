# !/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


class Douban:
    @staticmethod
    def get_post_from_link(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "lxml")
        return soup.find('div', 'review-content').contents[1]
