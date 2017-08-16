"""
用邮件的形式发送测试报告
"""

#coding = utf-8
import smtplib
#邮件内容
from email.mime.text import MIMEText
#邮件标题
from email.header import Header

#发送邮箱
sender = "1308476239@qq.com"
#接收邮箱
receiver = "570260538@qq.com"
#发送邮箱主题
subject = "python email test"
#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/密码
username = '1308476239@qq.com'
#QQ邮箱获取的不是明文密码，是授权码
password = 'cdqpkznhstvmjejc'

content = '<html><h1>你好！</h1></html>'
msg = MIMEText(content,'html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

smtp = smtplib.SMTP_SSL(smtpserver,465)
#链接邮件服务器
smtp.connect('smtp.qq.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
