#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver

class zentaoLoginTestCase(unittest.TestCase):

    # 判断是否登录成功，根据是否弹框
    def is_alert(self):
        try:
            self.driver.switch_to.alert
        except:
            return False
        else:
            sleep(2)
            self.driver.switch_to.alert.accept()
            return True


    # 前置条件，只需执行一次
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        # cls.driver.maximize_window()
        sleep(2)

    # 前置条件，每次执行用例前都需执行
    def setUp(self):
        self.driver.get('http://zt.huolail.com/user-login-Lw==.html')

    # 后置条件，只需执行一次
    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    # 后置条件，每次执行完用例都需执行
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    # 用例1：登录正确账号和密码
    def test01(self):
        self.driver.find_element_by_id('account').send_keys('tancichao')
        self.driver.find_element_by_name('password').send_keys('huolaile123')
        self.driver.find_element_by_id('submit').click()
        sleep(2)
        self.assertTrue(not self.is_alert())


    # 用例2：登录错误账号和密码
    def test02(self):
        self.driver.find_element_by_id('account').send_keys('aaaaaa')
        self.driver.find_element_by_name('password').send_keys('casads')
        self.driver.find_element_by_id('submit').click()
        sleep(2)
        self.assertTrue(self.is_alert())