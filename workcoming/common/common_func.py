#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from baseView.base import BaseView
import time, logging, csv


class Common(BaseView):

    def click(self, locator):
        '''重写click方法，主要是为了每次点击后检验新手操作引导'''
        element = self.findElement(locator)
        element.click()
        self.skip_or_next()

    def guide(self):
        '''检验引导图'''
        loc_guide_one = ('id', 'com.wnhz.workscoming:id/activity_guide_viewpager')  # 第一张图，用来等待时间的制定
        loc_guide_tostart = ('id', 'com.wnhz.workscoming:id/activity_guide_enter')  # 最后一张图，开启按钮

        try:
            self.findElement(loc_guide_one)
            for i in range(4):
                self.swipe_left()
                time.sleep(1)
            self.click(loc_guide_tostart)
            logging.info('==========引导图操作完成==========')
        except:
            logging.info('不是首次进入app，无引导图')
            pass

    def skip_or_next(self):
        '''跳过新手指导图的操作'''
        loc_greenhand = ('id', 'com.wnhz.workscoming:id/matte_iv')  # 新手指导的图片

        loc_skip = ('id', 'com.wnhz.workscoming:id/matte_space_top')  # 跳过
        # loc_next=('id','com.wnhz.workscoming:id/matte_space_bottom')#下一步

        try:
            self.findElement(loc_greenhand)
            self.click(loc_skip)
            logging.info('==========已跳过新手指引操作==========')
        except:
            logging.info('未检测到有新手指导图，直接下一步操作')
            pass

    def check_img(self):
        '''检测首页弹出图片'''
        loc_img = ('id', 'com.wnhz.workscoming:id/view_red_packet')  # 弹出的图片
        # loc_share_return=('id','com.wnhz.workscoming:id/title_left_image')#分享有礼返回

        logging.info('==========正在检测首页弹框==========')
        try:
            self.findElement(loc_img)
            self.driver.tap([(self.x * 0.5, self.y * 0.9)], 500)
            logging.info('首页弹框已点击关闭')
        except:
            logging.info('未检测到首页弹框，直接下一步操作')
            pass

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig')as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader,1):
                if index == line:
                    return row


if __name__ == '__main__':
    t=time.strftime('%Y-%m-%d %H:%M:%S')
    print(t)