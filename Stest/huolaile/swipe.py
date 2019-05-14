#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from huolaile.Capability_hll import *


# 获取屏幕尺寸
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 打印屏幕尺寸
l = get_size()
print('屏幕尺寸为：',l)


# 左滑
def swipeLeft():
    l = get_size()
    x1 = int(l[0] * 0.8)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.2)
    driver.swipe(x1, y1, x2, y1,500)

# 右滑
def swipeRight():
    l = get_size()
    x1 = int(l[0] * 0.8)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.2)
    driver.swipe(x2, y1, x1, y1,1000)

# 上滑
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.8)
    y2 = int(l[1] * 0.2)
    driver.swipe(x1, y1, x1, y2,1000)

# 下滑
def swipeDown():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.8)
    y2 = int(l[1] * 0.2)
    driver.swipe(x1, y2, x1, y1,1000)