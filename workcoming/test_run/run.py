#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest, time, logging, os, sys
from HTMLTestRunner_cn import HTMLTestRunner

path = os.path.abspath('../')
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports/'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + 'test_report_' + now + '.html'

with open(report_name, 'wb')as file:
    runner = HTMLTestRunner(stream=file, title='活来了测试报告', description='活来了安卓测试报告')
    runner.run(discover)
    logging.info('测试报告已生成，路径为：%s' % os.path.abspath(report_name))
