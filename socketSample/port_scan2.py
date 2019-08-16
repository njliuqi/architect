#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/16/19 4:23 PM
# @Author: edison

from __future__ import absolute_import

import multiprocessing
import socket

def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('localhost', port)) == 0:
        print('port {} is open'.format(port))

    s.close()


def worker(q):
    while not q.empty():
        port = q.get()
        try:
            scan(port)
        finally:
            q.task_done()


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    map(q.put, range(1, 65536))

    jobs = [multiprocessing.Process(target=worker, args=(q, )) for i in range(1, 100)]

    map(lambda x: x.start(), jobs)
