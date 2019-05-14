#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://newtest.huolail.com/Admin/User/login')
driver.maximize_window()
sleep(3)
driver.save_screenshot('fullscreen.png')
el = driver.find_element_by_id('vcode')
print(el.location)
print(el.size)

left = el.location['x']
right = el.location['x'] + el.size['width']
upper = el.location['y']
lower = el.location['y'] + el.size['height']

fullscreen = Image.open('fullscreen.png')
vcodescreen = fullscreen.crop((left, upper, right, lower))
vcodescreen.save('vcodescreen.png')
driver.quit()
