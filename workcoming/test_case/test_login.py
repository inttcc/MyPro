#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.myunit import StartEnd
from businessView.loginView import LoginView
import logging,unittest


class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    # @unittest.skip('skip test_error_user')
    def test_error_user(self):
        logging.info('**********test_error_user**********')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login(data[0], data[1])
        l.getScreenShot('test_error_user')
        self.assertTrue(not l.is_login_success())

    # @unittest.skip('skip test_error_psw')
    def test_error_psw(self):
        logging.info('**********test_error_psw**********')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login(data[0], data[1])
        l.getScreenShot('test_error_psw')
        self.assertTrue(not l.is_login_success())

    def test_login(self):
        logging.info('**********test_login**********')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login(data[0], data[1])
        l.getScreenShot('test_login')
        self.assertTrue(l.is_login_success())


if __name__ == '__main__':
    unittest.main()