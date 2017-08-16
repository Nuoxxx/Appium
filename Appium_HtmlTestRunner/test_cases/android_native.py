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

class AndroidNativeTests(unittest.TestCase):

    def setUp(self):
        app = os.path.abspath(
                os.path.join(os.path.dirname(__file__),
                             '/apps/selendroid-test-app.apk'))
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



    def test_activity(self):


        u"""打开EN Button，弹出对话框"""
        self.driver.find_element_by_accessibility_id('buttonTestCD').click()
        sleep(2)
        self.driver.find_element_by_id('button2').click()
        sleep(2)
        source = self.driver.page_source
        self.assertNotEqual(-1, source.find('Hello'))

        sleep(3)
        self.driver.find_element_by_accessibility_id('buttonTestCD').click()
        sleep(2)
        self.driver.find_element_by_id('button1').click()
        sleep(2)
        source = self.driver.page_source
        self.assertEqual(-1, source.find('Hello'))


    def test_register(self):
        u"""注册新用户"""
        self.driver.find_element_by_id('startUserRegistration').click()

        edit_texts = self.driver.find_elements_by_class_name('android.widget.EditText')
        edit_texts[0].send_keys('Amy')
        edit_texts[1].send_keys('yes@126.com')
        edit_texts[2].send_keys('123456')

        self.driver.find_element_by_id('btnRegisterUser').click()
        sleep(1)
        self.assertEqual(self.driver.find_element_by_id('label_username_data').text,"Amy")

    def test_text_input(self):
        u""" 在文本框中输入Hello，并获取文档判断"""
        text_input = self.driver.find_element_by_id('my_text_field')
        text_input.send_keys('Hello')
        sleep(2)
        self.assertEqual('Hello',text_input.text,'ERROR')

    def test_progress_bar(self):
        u""" 获取进度条，并打印出进度条中进度"""
        self.driver.find_element_by_id('waitingButtonTest').click()
        sleep(1)
        progressAct = self.driver.find_element_by_id('progress_percent').is_displayed()

        try:
            while(progressAct):
                print(progressAct)
                print(self.driver.find_element_by_id('progress_percent').text)
                sleep(2)
        except:
            print('进度条结束')
            return True

    def test_checkbox(self):
        u""" 判断checkbox是否勾选"""
        checkbox = self.driver.find_element_by_id('input_adds_check_box')

        if(checkbox.get_attribute('checked')):
            print('已经勾选')
            checkbox.click()
            sleep(2)
            checkbox.click()
        else:
            checkbox.click()
            sleep(2)
        print('ss')

        self.assertTrue(checkbox.get_attribute('checked'),'Error')


    def test_display_text_view(self):
        u""" 显示隐藏文本"""
        visibleButtonTest = self.driver.find_element_by_id('visibleButtonTest')
        visibleButtonTest.click()
        sleep(1)
        visibleText = self.driver.find_element_by_id('visibleTextView')
        self.assertEqual('Text is sometimes displayed',visibleText.text,'Wrong')

       # 'automationName':'uiautomator2'
    def test_toast(self):
        u"""获取Toast信息"""
        self.driver.find_element_by_id('showToastButton').click()

        message = '//*[@text=\'{}\']'.format("Hello selendroid toast!")
        element =WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,message)))

        self.assertEqual('Hello selendroid toast!',element.text)


    def test_popup(self):
        u"""获取popup弹框，暂时无法获取"""
        self.driver.find_element_by_id('showPopupWindowButton').click()
        sleep(2)
        dismiss = [(560,1180)]
        self.driver.tap(dismiss)
        sleep(5)


# alert dialog 可以通过UIAutomator的方式找到并点击
    def test_alert(self):
        u"""获取alert dialog"""
        self.driver.find_element_by_id('alertdialog').click()
        alert = self.driver.switch_to.alert
        # print(alert.text)
        print(alert)
        #可通过UIAutomatorviewer查看id,button1对应OK，button2对应NO
        self.driver.find_element_by_id('button1').click()
        sleep(2)
        #
        self.driver.find_element_by_id('alertdialog').click()
        alert = self.driver.switch_to.alert
        # print(alert.text)
        print(self.driver.page_source)
        print(alert)
        acceptButtons = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        acceptButtons[0].click()
        sleep(2)


    # App 崩溃
    def test_exception(self):
        self.driver.find_element_by_id('exceptionTestButton').click()
        sleep(1)
        self.driver.find_element_by_id('button1').click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



