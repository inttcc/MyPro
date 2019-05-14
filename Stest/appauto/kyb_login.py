#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from appauto.kyb_join import *


def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys(u'自学网2018')
    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

def my_login():
    try:
       driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
    except NoSuchElementException:
        login()
    else:
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("未登录")')
        except NoSuchElementException:
            driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
            driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
            driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
            driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
            login()
        else:
            driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
            login()


my_login()



