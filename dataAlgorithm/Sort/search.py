#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/13/19 5:15 PM
# @Author: edison

from __future__ import absolute_import

def binary_search_recursive(sorted_array, beg, end, val):
    if beg >= end:
        return -1
    mid = int((beg + end) / 2)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array, beg, mid, val)
    else:
        return binary_search_recursive(sorted_array, mid + 1, end, val)


def test_binary_search_recursive():
    # 我们测试所有值和边界条件
    a = list(range(10))
    for i in a:
        assert binary_search_recursive(a, 0, len(a), i) == i

    assert binary_search_recursive(a, 0, len(a), -1) == -1
    assert binary_search_recursive(a, 0, len(a), 10) == -1