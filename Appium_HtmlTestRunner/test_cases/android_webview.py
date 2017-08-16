import os
import glob
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.alert import Alert
import time
# import HTMLTestRunner

PLATFORM_VERSION = '5.1'

class AndroidWebViewTests(unittest.TestCase):

    def setUp(self):

        app = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                             '../apps/selendroid-test-app.apk'))
        desired_caps = {
            'app': app,
            'appPackage': 'io.selendroid.testapp',
            'appActivity': '.HomeScreenActivity',
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': '192.168.195.101:5555',
            #'autoautoAcceptAlerts':'true'
            # 'automationName':'uiautomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def test_webview(self):
        u"""测试webview"""
        self.driver.find_element_by_id('buttonStartWebview').click()
        print(self.driver.contexts)

        self.driver.switch_to.context('WEBVIEW')
        print(self.driver.current_context)
        print(self.driver.page_source)
        #这句很重要，不然会报错（Element is not currently interactable and may not be manipulated）
        self.driver.get('http://localhost:4450/')
        sleep(2)
        input_field = self.driver.find_element_by_id('name_input')
        # print("text:",input_field.text)
        sleep(1)
        input_field.clear()
        input_field.send_keys('Appium User')
        input_field.submit()
        sleep(3)

        # test that everything is a-ok
        source = self.driver.page_source
        self.assertNotEqual(-1, source.find('This is my way of saying hello'))
        self.assertNotEqual(-1, source.find('"Appium User"'))

    def test_xhtmlTestPage(self):
        u"""测试xhtmlTestPage"""
        self.driver.find_element_by_id('buttonStartWebview').click()
        print(self.driver.contexts)
        #弹出选择框
        self.driver.find_element_by_id('spinner_webdriver_test_data').click()
        sleep(1)

        choices = self.driver.find_elements_by_class_name('android.widget.TextView')
        choices[1].click()

        source = self.driver.page_source
        self.assertNotEqual(-1, source.find('XHTML Might Be The Future'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromName('test_webview')
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(AndroidWebViewTests('test_activity'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    # filename = '/Users/lihui/Documents/PycharmProjects/test/report/' + timestr + '.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='result',
    #     description='report'
    # )
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # fp.close()

    # suite = unittest.TestLoader().loadTestsFromName('AndroidWebViewTests.test_webview')
    # unittest.TextTestRunner(verbosity=2).run(suite)
