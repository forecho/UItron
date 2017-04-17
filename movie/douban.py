# !/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from common.translate import Translate
from movie.imdb import Imdb


class Douban:
    @staticmethod
    def get_post(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "lxml")
        content = soup.find('div', 'review-content')

        content = "".join(str(item) for item in content.contents)
        title = soup.find('span', {'property': 'v:summary'}).get_text()
        subject_link = soup.find('div', 'subject-title').a.get('href')
        # 详情页
        imdb_link = Douban.get_subject(subject_link)
        if imdb_link:
            # 获取 IMDB 详情
            imdb_subject = Imdb.get_subject(imdb_link)
            en_title = Translate.baidu(title)
            en_content = Translate.baidu(content)
            image = '<img class="size-medium" src="%s" alt="%s" width="253" height="400">' % (imdb_subject['movie_image'], imdb_subject['movie_title'])
            body = {'title': en_title + '(%s)' % imdb_subject['movie_title'], 'content': image + ' ' + en_content}
            return body
        return ''

    @staticmethod
    def get_subject(link):
        subject_page = requests.get(link)
        soup = BeautifulSoup(subject_page.content, "lxml")
        imdb_link = soup.find('div', 'subject').findAll('a')[-1].get('href')
        if ".imdb.com" in imdb_link:
            return imdb_link
        return ''
