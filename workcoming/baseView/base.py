#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import logging,time,os


class BaseView:
    '''二次封装'''

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.timeout = 2
        self.poll_frequency = 0.5

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            logging.error('locator参数类型错误，必须传元组类型：loc=("id","value")')
        else:
            logging.info('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
            element = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                lambda x: x.find_element(*locator))
            return element

    def findElements(self, locator):
        try:
            if not isinstance(locator, tuple):
                logging.error('locator参数类型错误，必须传元组类型：loc=("id","value")')
            else:
                logging.info('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
                elements = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_elements(*locator))
                return elements
        except:
            return []

    def sendKeys(self, locator, text):
        element = self.findElement(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self.findElement(locator)
        element.click()

    def clear(self, locator):
        element = self.findElement(locator)
        element.clear()

    def swipe_up(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        start_x = x * 0.5
        start_y = y * 0.8
        end_x = x * 0.5
        end_y = y * 0.2
        self.driver.swipe(start_x, start_y, end_x, end_y)
        logging.info('==========swipe   up==========')

    def swipe_down(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        start_x = x * 0.5
        start_y = y * 0.2
        end_x = x * 0.5
        end_y = y * 0.8
        self.driver.swipe(start_x, start_y, end_x, end_y)
        logging.info('==========swipe   down==========')

    def swipe_left(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        start_x = x * 0.8
        start_y = y * 0.5
        end_x = x * 0.2
        end_y = y * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y)
        logging.info('==========swipe   left==========')

    def swipe_right(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        start_x = x * 0.2
        start_y = y * 0.5
        end_x = x * 0.8
        end_y = y * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y)
        logging.info('==========swipe   right==========')

    def getScreenShot(self,module):#module为模块名称，即保存文件名称，可自定义
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        image_dir=os.path.abspath('../screenshots/%s_%s.png'%(module,now))
        self.driver.get_screenshot_as_file(image_dir)
        logging.info('%s已保存截图'%module)
        return image_dir



if __name__ == '__main__':
    from common.desired_caps import appium_desired
    driver = appium_desired()
    app = BaseView(driver)
    time.sleep(2)

    print(app.getScreenShot('启动页'))