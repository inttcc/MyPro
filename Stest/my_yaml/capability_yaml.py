#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

import yaml
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

file = open('desired_caps.yaml', 'r')
data = yaml.full_load(file)

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']
desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
# desired_caps['noReset'] = data['noReset']
# desired_caps['automationName'] = data['automationName']


driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
driver.implicitly_wait(3)


x = driver.get_window_size()['width']  # 屏幕宽
y = driver.get_window_size()['height']  # 屏幕高
print(x,y)

def swipeLeft():
    x1 = int(x * 0.8)
    y1 = int(y * 0.5)
    x2 = int(x * 0.2)
    driver.swipe(x1, y1, x2, y1, 500)


def swipeUp():
    x1 = int(x * 0.5)
    y1 = int(y * 0.9)
    y2 = int(y * 0.1)
    driver.swipe(x1, y1, x1, y2, 1000)

WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('com.mymoney:id/next_btn'))
for i in range(2):
    swipeLeft()
    sleep(1)
driver.find_element_by_id('com.mymoney:id/begin_btn').click()  # 点击开始
# driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()  # 点击更多
# driver.find_element_by_android_uiautomator('new UiSelector().text("更多")').click()

WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('com.mymoney:id/nav_btn_forth'))
driver.find_element_by_id('com.mymoney:id/nav_btn_forth').click()#点击设置

# WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('com.mymoney:id/content_container_ly'))
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('com.mymoney:id/more_member_ly'))

swipeUp()
sleep(1)
# driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
driver.find_element_by_id('com.mymoney:id/advance').click()

# driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
driver.find_element_by_id('com.mymoney:id/password_protect').click()

# driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()
driver.find_element_by_id('com.mymoney:id/ll_gesture_psd').click()

# TouchAction(driver).press(x=240, y=580).wait(1000)\
#     .move_to(x=540,y=580).wait(1000)\
#     .move_to(x=840,y=580).wait(1000)\
#     .move_to(x=840,y=880).wait(1000)\
#     .move_to(x=840,y=1180).wait(1000)\
#     .release().wait(500).perform()



for i in range(2):
    TouchAction(driver).press(x=200, y=300).wait(1000) \
    .move_to(x=350, y=600).wait(1000) \
    .move_to(x=500, y=300).wait(1000) \
    .move_to(x=200, y=450).wait(1000) \
    .move_to(x=500, y=600).wait(1000) \
    .move_to(x=350, y=300).wait(1000) \
    .move_to(x=200, y=600).wait(1000) \
    .move_to(x=500, y=450).wait(1000) \
    .move_to(x=350, y=450).wait(1000) \
    .release().perform()
    # TouchAction(driver).press(x=240, y=580).wait(1000) \
    # .move_to(x=540, y=1180).wait(1000) \
    # .move_to(x=840, y=580).wait(1000) \
    # .move_to(x=240, y=880).wait(1000) \
    # .move_to(x=840, y=1180).wait(1000) \
    # .move_to(x=540, y=580).wait(1000) \
    # .move_to(x=240, y=1180).wait(1000) \
    # .move_to(x=840, y=880).wait(1000) \
    # .move_to(x=540, y=880).wait(1000) \
    # .release().perform()