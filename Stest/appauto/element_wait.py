#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from appauto.kyb_login import *

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('') )

