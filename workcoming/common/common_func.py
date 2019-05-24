#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from baseView.base import BaseView
import time

class Common(BaseView):



    def guide(self):
        '''引导图的操作'''
        loc_guide_one=('id','com.wnhz.workscoming:id/activity_guide_viewpager')#第一张图，用来等待时间的制定
        loc_guide_tostart=('id','com.wnhz.workscoming:id/activity_guide_enter')#最后一张图，开启按钮


        self.findElement(loc_guide_one)
        for i in range(4):
            self.swipe_left()
            time.sleep(1)
        self.click(loc_guide_tostart)


    def skip_or_next(self):
        '''新手指导图的操作'''
        loc_greenhand=('id','com.wnhz.workscoming:id/matte_iv')#新手指导的图片

        loc_skip=('id','com.wnhz.workscoming:id/matte_space_top')#跳过
        loc_next=('id','com.wnhz.workscoming:id/matte_space_bottom')#下一步

        try:
            self.findElement(loc_greenhand)
            try:
                self.click(loc_skip)
            except:
                self.click(loc_next)
        except:
            pass