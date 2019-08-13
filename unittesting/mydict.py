#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/9/19 3:05 PM
# @Author: edison

from __future__ import absolute_import

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

