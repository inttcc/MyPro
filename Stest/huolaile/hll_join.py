#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from huolaile.swipe import *
from time import sleep

sleep(3)
for i in range(3):
    swipeLeft()
    sleep(1)

driver.find_element_by_id('com.wnhz.workscoming:id/activity_guide_enter').click()
sleep(2)


def target_click( x1, y1):  # x1,y1为你编写脚本时适用设备的实际坐标
    x_1 = x1 / 720  # 计算坐标在横坐标上的比例
    y_1 = y1 / 1280  # 计算坐标在纵坐标
    x = driver.get_window_size()['width']  # 获取设备的屏幕宽度
    y = driver.get_window_size()['height']  # 获取设备屏幕的高度
    print('点击的坐标点为：',(x_1 * x),(y_1 * y))
    driver.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作

close_img=target_click(360,1065)

driver.find_element_by_id('com.wnhz.workscoming:id/main_send_ll').click()
