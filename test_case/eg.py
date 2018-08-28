# coding=utf-8
from appium import webdriver
import unittest
import time

# 
# class ConnectTestLimao(unittest.TestCase):
#     
#     
#     def setUp(self):
desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
desired_caps['deviceName'] = '127.0.0.1:62001'  # 设备名称
desired_caps['appPackage'] = 'com.first.saccelerator'  # 测试app包名
desired_caps['appActivity'] = 'com.first.saccelerator.ui.activity.CheckPermissionsActivity'  # 测试appActivity
desired_caps['app'] = 'F://morenceshi(113-A)20180709.apk'
desired_caps['noReset'] = True  #如果没有回从安装后的界面开始
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
driver.implicitly_wait(10)
time.sleep(10)   
                              
#     def test_start(self):

#            
#            
#     def tearDown(self):
driver.quit()
#     
#    
# if __name__ == "__main__":
#     unittest.main()    
     