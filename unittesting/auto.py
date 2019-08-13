#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time :  8/9/19 2:51 PM
# @Author: edison

from __future__ import absolute_import

from .widget import Widget
import unittest

"""
    用import语句引入unittest模块。
    让所有执行测试的类都继承于TestCase类，可以将TestCase看成是对特定类进行测试的方法的集合。
    在setUp()方法中进行测试前的初始化工作，并在tearDown()方法中执行测试后的清除工作，
    setUp()和tearDown()都是TestCase类中定义的方法。
    在testSize()中调用assertEqual()方法，对Widget类中getSize()方法的返回值和预期值进行比较，
    确保两者是相等的，assertEqual()也是TestCase类中定义的方法。
    提供名为suite()的全局方法，PyUnit在执行测试的过程调用suit()方法来确定有多少个测试用例需要被执行，
    可以将TestSuite看成是包含所有测试用例的一个容器。
"""
class WidgetTestCase(unittest.TestCase):

    def SetUP(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')