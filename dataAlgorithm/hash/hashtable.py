#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/9/19 3:19 PM
# @Author: edison

from __future__ import absolute_import

from dataAlgorithm.Array.array_and_list import Array

class Slot(object):
    """定义一个 hash 表 数组的槽
    注意，一个槽有三种状态，看你能否想明白
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """
    def __init__(self, key, value):
        self.key, self.value = key, value

class HashTable(object):
    UNSET = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNSET)   # keep 2**i
        self.length = 0

    @property
    def __load_factor(self):
        # load_factor 超过0.8 重新分配
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def __hash(self, key):
        return abs(hash(key)) % len(self._table)


    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNSET:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 + 1) % _len

        return None

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len

        return index

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNSET)


    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False

        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self.__load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNSET)
        self.length = 0
        for slot in old_table:
            if slot is not HashTable.UNSET and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value


    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value


    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNSET):
                yield slot.key



class DictADT(HashTable):

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNSET):
                yield slot

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def values(self):
        for slot in self._iter_slot():
            yield slot.value

def test_hash_table():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)
    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get('hehe') is None

    h.remove('a')
    assert h.get('a') is None
    assert sorted(list(h)) == ['b', 'c']

    n = 50
    for i in range(n):
        h.add(i, i)

    for i in range(n):
        assert h.get(i) == i


if __name__ == '__main__':
    print(
        'beg',
        test_hash_table(),
        'end',
    )