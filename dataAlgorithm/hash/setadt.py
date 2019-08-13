#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/13/19 4:38 PM
# @Author: edison

from __future__ import absolute_import


from dataAlgorithm.Array.array_and_list import Array
from dataAlgorithm.hash.hashtable import Slot, HashTable


class SetADT(HashTable):
    def add(self, key):
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a in new_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a not in new_set:
                new_set.add(element_a)
        return new_set

    def __or__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)

        return new_set


def test_set_adt():
    sa = SetADT()
    sa.add(1)
    sa.add(2)
    sa.add(3)
    assert 1 in sa    # 测试  __contains__ 方法，实现了 add 和 __contains__，集合最基本的功能就实现啦

    sb = SetADT()
    sb.add(3)
    sb.add(4)
    sb.add(5)

    assert sorted(list(sa & sb)) == [3]
    assert sorted(list(sa - sb)) == [1, 2]
    assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    test_set_adt()