#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/13/19 5:24 PM
# @Author: edison

from __future__ import absolute_import


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_idx = 1
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j

        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]


def insert_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
        print(seq)

def quick_sort():
    pass