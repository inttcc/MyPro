#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
sleep(2)
driver.quit()