#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from huolaile.hll_join import *

driver.find_element_by_id('com.wnhz.workscoming:id/newlogin_phonenumber').clear()
driver.find_element_by_id('com.wnhz.workscoming:id/newlogin_phonenumber').send_keys('13979962205')
driver.find_element_by_id('com.wnhz.workscoming:id/newlogin_code').send_keys('123456')
driver.find_element_by_id('com.wnhz.workscoming:id/newlogin_loginbtn').click()



#定位设置
driver.find_element_by_id('com.wnhz.workscoming:id/search_top_city_ll').click()
myaddress=driver.find_elements_by_id('com.wnhz.workscoming:id/company_name_ll')
myaddress[1].click()