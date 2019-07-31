#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  7/29/19 4:10 PM
# @Author: edison

from __future__ import absolute_import

import gevent
from gevent import monkey

monkey.patch_all()


from urllib.request import urlopen

def f(url):
    print('GET:  %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print("%d bytes received from %s." % (len(data), url))



gevent.joinall([
    gevent.spawn(f, 'http://www.python.org'),
    gevent.spawn(f, 'http://www.sina.com'),
    gevent.spawn(f, 'http://www.sohu.com'),
])