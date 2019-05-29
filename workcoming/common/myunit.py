#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest, logging, time

from common.desired_caps import appium_desired


class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('**********setUp**********')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('**********tearDown**********')
        time.sleep(5)
        self.driver.close_app()
