#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
setting = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(setting).perform()
driver.find_element_by_link_text('搜索设置').click()
sleep(2)
# driver.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
driver.find_element_by_css_selector('#nr>option:last-child').click()
sleep(2)
driver.find_element_by_link_text('保存设置').click()
sleep(2)
try:
    web_alert=driver.switch_to.alert
except:
    print('没有弹窗')
else:
    print('弹出文字：'+web_alert.text)
    web_alert.accept()
sleep(3)
driver.quit()
