# !/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


class Imdb:
    @staticmethod
    def get_subject(link):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "lxml")
        title = soup.find('div', 'title_wrapper').find('h1').get_text()
        try:
            image = soup.find('div', 'slate_wrapper').find('img').get('src')
        except AttributeError:
            image = soup.find('div', 'minPosterWithPlotSummaryHeight').find('img').get('src')

        # tags = []
        # for tag in soup.find('div', 'title_wrapper').findAll('span', 'itemprop'):
        #     tags.append(tag.get_text())
        # return {'title': title, 'image': image, 'tags': tags}
        return {'movie_title': title, 'movie_image': image}
