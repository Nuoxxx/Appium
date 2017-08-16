#coding:utf-8
import unittest
import os,sys
from appium import webdriver
import time
import keyword
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PLATFORM_VERSION = '6.0'

class Multi_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #当前文件地址
        filepath = os.path.abspath(__file__)
        apppath = os.path.abspath(os.path.join(filepath,'../../apps/zhongxiang.apk'))

        desired_caps = {
           # 'app': apppath,
            'appPackage':'com.ccvt.dajia',
            'appActivity':'.ui.WelcomeActivity',
            'platformName':'Android',
            'platformVersion':PLATFORM_VERSION,
            'deviceName':'Y9K0214B01008877',
            'unicodeKeyboard':'True',
            'resetKeyboard':'True'
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    #滑动引导图，进入APP首页
    def swipe_guidance(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        for i in range(0,4):
            time.sleep(2)
            print(i)
            self.driver.swipe(width*4/5,height/2,width*1/5,height/2)
        # time.sleep(3)
        # self.driver.swipe(800, 800, 200, 800)
        # time.sleep(2)
        # self.driver.swipe(800, 800, 200, 800)
        # time.sleep(2)
        # self.driver.swipe(800, 800, 200, 800)
        time.sleep(2)
        self.driver.find_element_by_id('btn_close_guide').click()

    def test_Numberlogin(self):
        self.swipe_guidance()
        time.sleep(3)
        self.driver.find_element_by_id('header_my_center_img').click()

        if(self.driver.find_element_by_id('tv_sign').is_displayed()):
            #未登录
            print(self.driver.find_element_by_id('tv_sign').text)
            self.driver.find_element_by_id('head_img').click()
            self.login()

            self.assertIsNotNone(self.driver.find_element_by_id('head_img'), 'error')
            # 回到我的页面
            time.sleep(1)
            self.driver.find_element_by_id('header_my_center_img').click()
            time.sleep(1)
            self.driver.find_element_by_id('my_img').click()
            self.assertIsNotNone(self.driver.find_element_by_id('sex_img'), 'login error')

        else:
            print('已登录')
    #微博登录,没办法重载微博登录界面，无法获取界面数据
    # def test_WeiboLogin(self):
    #     time.sleep(1)
    #     self.driver.find_element_by_id('header_my_center_img').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id('settingBt').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id('switch_user').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id('weiboLogin').click()
    #     time.sleep(10)
    #     #此处需要填入url
    #     self.driver.get()
    #     print("contexts:",self.driver.contexts)
    #     self.driver.switch_to.context('WEBVIEW')
    #
    #     self.driver.find_element_by_id('userId').send_keys('1308476239@qq.com')
    #     self.driver.find_element_by_id('passwd').send_keys('gaoxing1210')
    #     # 登录按钮
    #     time.sleep(2)
    #     self.driver.find_element_by_class_name('btnP').click()
    #
    #     self.driver.switch_to.context('nativeapp')
    #
    #     # 等待跳转回到设置界面
    #     WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_activity == '.ui.SettingActivity',
    #                                          'error')
    #
    #     print(u'QQ登录')
    #     self.driver.find_element_by_id('header_left_img').click()
    #     # 回到我的页面
    #     time.sleep(1)
    #     self.driver.find_element_by_id('header_my_center_img').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id('my_img').click()
    #     self.assertIsNotNone(self.driver.find_element_by_id('sex_img'), 'login error')


    # QQ登录
    def test_QQLogin(self):
        time.sleep(1)
        self.driver.find_element_by_id('header_my_center_img').click()
        time.sleep(1)
        self.driver.find_element_by_id('settingBt').click()
        time.sleep(1)
        self.driver.find_element_by_id('switch_user').click()
        time.sleep(1)
        self.driver.find_element_by_id('qqLogin').click()
        #等待跳转到QQ界面
        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_activity == 'com.tencent.open.agent.AuthorityActivity','error')
        #登录按钮
        buttons = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        buttons[1].click()
        # 等待跳转回到设置界面
        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_activity == '.ui.SettingActivity','error')

        print(u'QQ登录')
        self.driver.find_element_by_id('header_left_img').click()
        # 回到我的页面
        time.sleep(1)
        self.driver.find_element_by_id('header_my_center_img').click()
        time.sleep(1)
        self.driver.find_element_by_id('my_img').click()
        self.assertIsNotNone(self.driver.find_element_by_id('sex_img'), 'login error')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tearDown')

    def login(self):

        time.sleep(1)
        self.driver.find_element_by_id('accountTv').send_keys('18565687532')
        time.sleep(2)
        self.driver.find_element_by_id('passwordTv').send_keys('123456')
        #收起键盘
        self.driver.press_keycode(66)
        time.sleep(1)

        self.driver.find_element_by_id('loginBt').click()
        time.sleep(3)




if __name__ == '__main__':
    unittest.main()
