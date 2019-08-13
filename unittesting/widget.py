#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/9/19 2:49 PM
# @Author: edison

from __future__ import absolute_import


class Widget:
    def __init__(self, size=(40, 40)):
        self._size = size

    def getSize(self):
        return self._size

    def resize(self, width, height):
        if width == 0 or height < 0:
            raise ValueError("illegal size")
        self._size = (width, height)

    def dispose(self):
        pass
