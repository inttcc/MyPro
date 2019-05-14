#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62026'  # GWY0217710001353
desired_caps['platformVersion'] = '5.1.1'
desired_caps['app'] = r'C:\Users\Administrator\Desktop\mymoney.apk'
desired_caps['appPackage'] = 'com.mymoney'
desired_caps['appActivity'] = 'com.mymoney.biz.splash.SplashScreenActivity'
# desired_caps['noReset'] = 'False'#False

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y

def swipeLeft():
    l = get_size()
    x1 = int(l[0] * 0.8)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.2)
    driver.swipe(x1, y1, x2, y1,500)

def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.8)
    y2 = int(l[1] * 0.2)
    driver.swipe(x1, y1, x1, y2,1000)

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))
for i in range(2):
    swipeLeft()
    sleep(0.5)
driver.find_element_by_id('com.mymoney:id/begin_btn').click()#点击开始
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()#点击更多

