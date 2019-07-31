#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  7/29/19 3:54 PM
# @Author: edison

from __future__ import absolute_import

import zerorpc

c = zerorpc.Client()

c.connect("tcp://192.168.9.22:7788")

print(c.hello('RPC'))
