#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = 'https://kyfw.12306.cn/otn/leftTicket/init'
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
sleep(1)

# 点击登录按钮
driver.find_element_by_id('login_user').click()
sleep(1)

# 点击账号登录
driver.find_element_by_css_selector('.login-hd-account > a:nth-child(1)').click()
sleep(1)

# 输入用户名
driver.find_element_by_id('J-userName').send_keys('13979962205')
# 输入密码
driver.find_element_by_id('J-password').send_keys('BS19951221tcc')
print('请手动选择验证码')
sleep(10)

# 点击登录
driver.find_element_by_id('J-login').click()
print('登录成功')
sleep(3)

# 跳转预定页面
js1 = 'document.querySelectorAll("#J-chepiao > a[class = nav-hd]")[0].click();'
driver.execute_script(js1)
js2 = 'document.querySelectorAll(".nav_dan > a[name = g_href]")[0].click();'
driver.execute_script(js2)
sleep(3)

# 选择出发
driver.find_element_by_css_selector('#fromStationText').click()
driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.CONTROL + 'a')
driver.find_element_by_css_selector('#fromStationText').send_keys('赣州')
sleep(1)
driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER)
sleep(1)

# 选择目的地
driver.find_element_by_css_selector('#toStationText').click()
driver.find_element_by_css_selector('li.ac_even:nth-child(14)').click()
sleep(1)

# 选择出发日
driver.find_element_by_css_selector('#date_icon_1').click()
driver.find_element_by_css_selector(
    'div.cal:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1)').click()
sleep(1)

# 车次类型勾选
driver.find_element_by_css_selector('input[value = T]').click()
driver.find_element_by_css_selector('input[value = K]').click()

i = 1
while True:
    driver.find_element_by_css_selector('#query_ticket').click()  # 点击查询
    c1 = driver.find_element_by_css_selector('#YW_630000T1700N')  # T170   #YW_630000T1700N
    c2 = driver.find_element_by_css_selector('#YW_650000T1020D')  # T102   #YW_650000T1020D
    c3 = driver.find_element_by_css_selector('#YW_570000K47020')  # K470   #YW_570000K47020
    if c1.text in ['无', '--', '*'] and c2.text in ['无', '--', '*'] and c3.text in ['无', '--', '*']:
        print('抢票%d次' % (i))
        sleep(1)
        i += 1
    else:
        print('有票，正在预定中。。。')
        # 购票
        # 如果T170有票
        if c1.text not in ['无', '--', '*']:
            driver.find_element_by_css_selector('#ticket_630000T1700N > td:nth-child(13) > a:nth-child(1)').click()
            # 乘车人选择
            driver.find_element_by_css_selector('#normalPassenger_5').click()
            # 提交订单
            driver.find_element_by_css_selector('#submitOrder_id').click()
            sleep(5)
            driver.find_element_by_xpath('//*[@id="qr_submit_id"]').click()#确认
            sleep(5)
            print('T170抢票成功，请尽快支付')
            break

        # 如果T120有票
        if c2.text not in ['无', '--', '*']:
            driver.find_element_by_css_selector('#ticket_650000T1020D > td:nth-child(13) > a:nth-child(1)').click()
            # 乘车人选择
            driver.find_element_by_css_selector('#normalPassenger_5').click()
            # 提交订单
            driver.find_element_by_css_selector('#submitOrder_id').click()
            sleep(5)
            driver.find_element_by_xpath('//*[@id="qr_submit_id"]').click()
            sleep(5)
            print('T120抢票成功，请尽快支付')
            break

        # 如果K470有票
        if c3.text not in ['无', '--', '*']:
            driver.find_element_by_css_selector('#ticket_570000K47020 > td:nth-child(13) > a:nth-child(1)').click()
            # 乘车人选择
            driver.find_element_by_css_selector('#normalPassenger_5').click()
            # 提交订单
            driver.find_element_by_css_selector('#submitOrder_id').click()
            sleep(5)
            driver.find_element_by_xpath('//*[@id="qr_submit_id"]').click()
            sleep(5)
            print('K470抢票成功，请尽快支付')
            break

# driver.quit()
