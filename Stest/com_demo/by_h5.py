#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62026'  # GWY0217710001353
desired_caps['platformVersion'] = '5.1.1'
# desired_caps['udid']='127.0.0.1:62029'#bec6800

desired_caps['app'] = r'C:\Users\Administrator\Desktop\dr.fone3.2.0.apk'
desired_caps['appPackage'] = 'com.wondershare.drfone'
desired_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'

desired_caps['noReset'] = 'False'#False
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()
WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()
WebDriverWait(driver,10).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
# contexts=driver.contexts
print(driver.contexts)


driver.switch_to.context('WEBVIEW_com.wondershare.drfone')     #'WEBVIEW_com.wondershare.drfone'
driver.find_element_by_id('email').send_keys('shuqing2018@163.com')
driver.find_element_by_class_name('btn_send').click()

driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()