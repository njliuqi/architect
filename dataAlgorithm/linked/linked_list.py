#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/13/19 11:37 AM
# @Author: edison

from __future__ import absolute_import

class Node(object):
    def __init__(self, value=None, nex=None):
        self.value = value
        self.nex = nex

    def __str__(self):
        return '<Node: value: {}, next={}'.formt(self.value, self.next)


class LinkedList(object):
    """
        [root] -> [node0] ->[node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()   # 默认root节点指向None
        self.tailnode = Node
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('linked list is full')

        node = Node(value)
        tailnode = self.tailnode

        if tailnode is None:

            self.root.nex = node
        else:
            tailnode.nex = node

        self.tailnode = node

        self.length += 1

    def appendlift(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('linked list is full')
        node = Node(value)

        if self.tailnode is None:
            self.tailnode = node

        head = self.root.nex
        self.root.nex = node
        node.nex = head
        self.length += 1


    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        curnode = self.root.nex
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.nex

        if curnode is not None:
            yield curnode

    def remove(self):  # O(n)
        pass

    def find(self, value):  # O(n)
        """

        :param value:
        :return:
        """
        index = 0

        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1    # not found

    def popleft(self): # O(1)
        """
            delete linked list first element.
        :return:
        """
        if self.root.nex is None:
            raise Exception('pop from empty Linked list')
        head = self.root.nex
        self.root.nex = head.nex
        self.length -= 1
        value = head.value

        if self.tailnode is head:
            self.tailnode = None
        del head

        return value

    def clear(self):
        for node in self.iter_node():
            del node

        self.root.nex = None
        self.length = 0
        self.tailnode = None


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_reverse()


