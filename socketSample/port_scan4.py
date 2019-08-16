#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/16/19 4:39 PM
# @Author: edison

from __future__ import absolute_import

import nmap

import IPy

ip = IPy.IP('192.168.9.0/24')
print(ip.len())

for x in ip:
    print(x)