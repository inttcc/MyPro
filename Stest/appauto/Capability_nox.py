#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62026'  # GWY0217710001353
desired_caps['platformVersion'] = '5.1.1'
# desired_caps['udid']='127.0.0.1:62029'#bec6800

desired_caps['app'] = r'C:\Users\Administrator\Desktop\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

desired_caps['noReset'] = 'True'#False
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)

