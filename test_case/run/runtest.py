# coding=utf-8
import unittest
import Login
import Uitest
import HTMLTestRunner
import Connect
import ChangeService
import Ad
#构造测试集
suite = unittest.TestSuite()
suite.addTest(Login.LoginTestLimao('test_login'))
suite.addTest(Uitest.UITestlimao('test_ui'))
suite.addTest(Connect.ConnectTestLimao('test_Connect'))
suite.addTest(ChangeService.ServiceTestlimao('test_ChangeService'))
suite.addTest(Ad.AdTestLimao('test_Ad'))

if __name__ == '__main__':  
    filename = 'F:\\4\\app.html'
    fb = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=u'狸猫自动化测试报告', description=u'我们不一样',tester=u'唐诚')
    runner.run(suite)
    fb.close()