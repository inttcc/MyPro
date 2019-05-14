#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
# from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62026'  # GWY0217710001353
desired_caps['platformVersion'] = '5.1.1'
# desired_caps['udid']='127.0.0.1:62029'#bec6800

desired_caps['app'] = r'C:\Users\Administrator\Desktop\app_310\huolaile4_3_10.apk'
desired_caps['appPackage'] = 'com.wnhz.workscoming'
desired_caps['appActivity'] = 'com.wnhz.workscoming.start.activitys.StartActivity'

desired_caps['noReset'] = 'False'#False
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


