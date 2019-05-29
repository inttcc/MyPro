#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from common.common_func import Common


class LoginView(Common):
    loc_my = ('id', 'com.wnhz.workscoming:id/main_my_ll')  # 我的模块
    loc_my_sex = ('id', 'com.wnhz.workscoming:id/iv_myInfo_sex')  # 性别图标，用来判断是否登录，未登录没有该图标
    loc_my_head = ('id', 'com.wnhz.workscoming:id/iv_myInfo_head')  # 头像
    loc_back_login = ('id', 'com.wnhz.workscoming:id/person_info_backlogin')  # 退出账号
    loc_sure_quit = ('id', 'com.wnhz.workscoming:id/dialog_aler_enter')  # 确定退出账号
    loc_username = ('id', 'com.wnhz.workscoming:id/newlogin_phonenumber')  # 账号
    loc_password = ('id', 'com.wnhz.workscoming:id/newlogin_code')  # 密码
    loc_login_button = ('id', 'com.wnhz.workscoming:id/newlogin_loginbtn')  # 登录按钮
    loc_alert_submit = ('id', 'com.wnhz.workscoming:id/dia_submit')  # 提示框提交按钮

    def is_login(self):
        '''判断是否登录'''
        self.click(self.loc_my)
        try:
            self.findElement(self.loc_my_sex)
            return True
        except:
            return False

    def login(self, username, password):
        self.guide()
        self.check_img()
        if self.is_login():
            self.click(self.loc_my_head)
            self.click(self.loc_back_login)
            self.click(self.loc_sure_quit)
        else:
            self.click(self.loc_my_head)
        self.sendKeys(self.loc_username, username)
        self.sendKeys(self.loc_password, password)
        self.click(self.loc_login_button)

    def is_login_success(self):
        '''是否登录成功，用弹框判断'''
        try:
            self.findElement(self.loc_alert_submit)
            return False
        except:
            return True



if __name__ == '__main__':
    from common.desired_caps import appium_desired

    driver = appium_desired()
    app = LoginView(driver)
    app.guide()
    app.check_img()
    csv_file = '../data/account.csv'
    data = app.get_csv_data(csv_file, 1)
    app.login(data[0], data[1])
    app.getScreenShot('登录')
