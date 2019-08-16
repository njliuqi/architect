#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/16/19 4:01 PM
# @Author: edison

from __future__ import absolute_import

import socket
import threading

def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('localhost', port)) == 0:
        print('port {} is open'.format(port))

    s.close()


if __name__ == '__main__':

    threads = [threading.Thread(target=scan, args=(i,)) for i in range(1, 65536)]

    map(lambda x:x.start(), threads)