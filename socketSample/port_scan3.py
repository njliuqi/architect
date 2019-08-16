#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/16/19 4:31 PM
# @Author: edison

from __future__ import absolute_import

from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()

import gevent

import socket


def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('localhost', port)) == 0:
        print('port {} is open'.format(port))

    s.close()


if __name__ == '__main__':
    threads = [gevent.spawn(scan, i) for i in range(1, 65536)]
    gevent.joinall(threads)


    # pool

    # pool = Pool(500)
    # pool.map(scan, range(1, 65536))
    # pool.join()
