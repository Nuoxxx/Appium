# coding = utf-8
"""
获取最新的测试报告
"""
import os,datetime,time

# result_dir = 'D:\\Selenium_project\\report'

result_dir = os.path.abspath(os.path.join(os.path.abspath(__file__),"../../report"))
lists = os.listdir(result_dir)
#fn就是lists中的元素，自动遍历
lists.sort(key = lambda fn: os.path.getmtime(result_dir+"\\"+fn)
if not os.path.isdir(result_dir+"\\"+fn) else 0)

print('最新的文件为：'+lists[-1])
file = os.path.join(result_dir,lists[-1])
print(file)