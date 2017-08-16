#coding:utf-8
import unittest
from appium import webdriver
import os,sys,time
# sys.path.append('\test_case')
from test_cases import Login


class Publish_activity(unittest.TestCase):

    def setUp(self):
        filepath = os.path.abspath(__file__)
        app = os.path.abspath(os.path.join(filepath, '../../apps/zhongxiang.apk'))

        desired_caps = {
            'platformName' : 'Android',
            'platformVersion':'6.0',
            'deviceName':'Y9K0214B01008877',
            'app':app,
            'appPackage':'com.ccvt.dajia',
            'appActivity':'.ui.WelcomeActivity',
            'unicodeKeyboard':'True',
            'resetKeyboard':'True'
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def test_publish_activity(self):
        time.sleep(2)
        Login.Multi_login.swipe_guidance(self)
        time.sleep(2)
        self.driver.find_element_by_id('publish_img').click()

        time.sleep(1)
        #判断是否登录
        if(self.driver.find_element_by_id('accountTv').is_displayed()):
            print('not login')
            Login.Multi_login.login(self)
        else:
            print('already login')


        print('enter publish page')

        els1 = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        print("len els1:",len(els1))

        els = self.driver.find_elements_by_xpath('//android.widget.LinearLayout')
        print('els:',len(els))
        self.driver.scroll(els[len(els)-1],els[0])
        self.assertTrue(self.driver.find_element_by_id('agreement_tv').text,u'同意《大加众享使用协议》')



    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
