import sys,time,os
import smtplib
import unittest
#由于模块和当前文件不在一个目录下，将模块添加到程序中
# sys.path.append('\Appium_HtmlTestRunner')
from Appium_Learn.Appium_HtmlTestRunner.test_cases import android_native
from Appium_Learn.Appium_HtmlTestRunner.test_cases import android_webview

import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(android_native.AndroidNativeTests))
#新增某个用例
# suite.addTest(android_native.AndroidNativeTests('test_activity'))
#新增某个.py文件中类下面的所有用例
suite.addTests(unittest.makeSuite(android_webview.AndroidWebViewTests))

now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())

filename = os.path.abspath(os.path.join(os.path.abspath(__file__),'../report/'+now+"result.html"))
fp = open(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='selenium_app_test',description=u'测试')
runner.run(suite)