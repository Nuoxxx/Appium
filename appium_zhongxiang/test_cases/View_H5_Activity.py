import unittest
from appium import webdriver
import os,sys
from time import sleep
from test_cases import Login


class view_activity(unittest.TestCase):
    def setUp(self):
        filepath = os.path.abspath(__file__)
        app = os.path.abspath(os.path.join(filepath, '../../apps/zhongxiang.apk'))

        desired_caps = {
            'platformName' : 'Android',
            'platformVersion':'6.0',
            'deviceName':'Y9K0214B01008877',
            # 'app':app,
            'appPackage':'com.ccvt.dajia',
            'appActivity':'.ui.WelcomeActivity',
            'unicodeKeyboard':'True',
            'resetKeyboard':'True'
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def test_view_activity(self):
        Login.Multi_login.swipe_guidance(self)

        sleep(3)
        els = self.driver.find_elements_by_xpath("//android.widget.LinearLayout")

        print(len(els))

        els[11].click()
        sleep(10)

        print(self.driver.contexts)

        if 'WEBVIEW' not in self.driver.contexts:
            print('no webview')

        else:
            self.driver.switch_to.context('WEBVIEW')
            print(self.driver.page_source)

            time = self.driver.find_elements_by_class_name('a_time')
            # self.assertEqual(time.te)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
