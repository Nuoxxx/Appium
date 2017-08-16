# coding = utf-8

import unittest
import HTMLTestRunner
import os,time,datetime,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
sys.path.append('\test_cases')
from test_cases import android_native
from test_cases import android_webview

#定义发送邮件
def sendmail(file_new):
    # 发送邮箱
    sender = "1308476239@qq.com"
    # 接收邮箱
    receiver = "570260538@qq.com"
    #
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject'] = u'测试报告'
    #定义发送时间
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户/密码
    username = '1308476239@qq.com'
    password = 'cdqpkznhstvmjejc'
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # 链接邮件服务器
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out')

#查找测试报告，调用发邮件功能
def sendreport():
    result_dir = "/Users/xuxuexia/Documents/PythonEX/Selenium_project/report/"

    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "/" + fn)
    if not os.path.isdir(result_dir + "/" + fn) else 0)

    print('最新的文件为：' + lists[-1])
    file = os.path.join(result_dir, lists[-1])
    print(file)
    sendmail(file)

def getsuite():
    suite = unittest.TestSuite()

    # suite.addTests(unittest.makeSuite(android_native.AndroidNativeTests))
    # 新增某个用例
    suite.addTest(android_native.AndroidNativeTests('test_activity'))
    # 新增某个.py文件中类下面的所有用例
    suite.addTests(unittest.makeSuite(android_webview.AndroidWebViewTests))


    return suite


if __name__ == "__main__":
    #
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())

    filename ="/Users/xuxuexia/Documents/PythonEX/Selenium_project/report/"+now + "_result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='selenium_app_test', description=u'测试')
    runner.run(getsuite())
    sendreport()
