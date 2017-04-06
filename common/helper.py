# !/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


class Helper:
    def __init__(self):
        pass

    @staticmethod
    def merge_two_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    @staticmethod
    def config(key):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        try:
            value = cfg[key]
        except Exception:
            return ''
        return value