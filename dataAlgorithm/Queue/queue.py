#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/13/19 1:42 PM
# @Author: edison

from __future__ import absolute_import

from collections import deque

from dataAlgorithm.linked.linked_list import Node, LinkedList

class EmptyError(Exception):
    pass

class Queue:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_link_list = LinkedList()


    def __len__(self):
        return self._item_link_list

    def push(self, value):  # O(1)
        return self._item_link_list.append(value)

    def pop(self):
        if len(self) <=0:
            raise EmptyError('empty queue')
        return self._item_link_list.popleft()




