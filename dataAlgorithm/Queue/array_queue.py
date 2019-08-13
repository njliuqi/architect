#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/13/19 1:32 PM
# @Author: edison

from __future__ import absolute_import


from dataAlgorithm.Array.array_and_list import Array

class FullError(Exception):
    pass

class ArrayQueue(object):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value


def test_queue():
    import pytest    # pip install pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as excinfo:   # 我们来测试是否真的抛出了异常
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == 5

    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)

    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0


