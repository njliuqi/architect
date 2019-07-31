#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  7/29/19 4:36 PM
# @Author: edison

from __future__ import absolute_import

import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('task %s done' % pid)


def synchronous():
    for i in range(0, 5):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(0, 5)]
    gevent.joinall(threads)
    print('Synchronous:')
    synchronous()
    print('Asynchronous:')
    asynchronous()