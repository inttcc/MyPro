#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appauto.swipe_action import *


def check_cancelBtn():
    print('check cancelBtn...')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()


def check_skipBtn():
    print('check skipBtn...')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()


def slide():
    try:
        driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        pass
    else:
        for i in range(2):
            swipeLeft()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()


check_cancelBtn()
slide()
# check_skipBtn()
