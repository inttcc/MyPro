#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import yaml,os,logging,logging.config
from appium import webdriver

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG,)
logging= logging.getLogger()


def appium_desired():
    with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.full_load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = os.path.abspath(data['app'])
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    logging.info('==========start   app==========')
    return driver


if __name__ == '__main__':
    driver=appium_desired()