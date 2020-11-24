import unittest
import time
import yagmail
from HTMLTestRunner import HTMLTestRunner
def send_mail(report):
    yag=yagmail.SMTP(user="382927895@qq.com",password="yakoyffvahzdbiaf",host='smtp.qq.com')
    print("登录成功")
    subject="主题，自动化测试报告"
    contents="正文，请查看附件"
    yag.send('382927895@qq.com',subject,contents,[report])
    print('email has send out!')
test_dir="D://drivers//unittest//test_case"
result_dir="D://drivers//unittest//test_report//"
suits=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__=='__main__':
    test_dir="D://drivers//unittest//test_case"
    result_dir="D://drivers//unittest//test_report//"
    suits=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now_time=time.strftime("%Y-%m-%d %H_%M_%S")
    html_report=result_dir+now_time+'result.html'
    fp=open(html_report,'wb')
    runner=HTMLTestRunner(stream=fp,title="百度搜索测试报告",description="运行环境:Windows 10,Firefox 浏览器")
    runner.run(suits)
    fp.close()
    #send_mail("D://drivers//unittest//test_report//1.txt")
    send_mail(html_report)