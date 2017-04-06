# !/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon


class CrawlerResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex)

        try:
            resp.body = {"test": "收到"}
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Could not decode the request body. The ''JSON was incorrect.')


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
crawler = CrawlerResource()

app.add_route('/', crawler)
