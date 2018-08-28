# coding=utf-8
from appium import webdriver
import unittest

class AdTestLimao(unittest.TestCase):
    def setUp(self):
        desired_caps = {
                    'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'4.4.2',
                    'appPackage':'com.first.saccelerator',
                    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
                    'noReset':True}      
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  
        self.driver.implicitly_wait(20)                
    def test_Ad(self):
        driver = self.driver
        #打开广告页
        driver.find_element_by_id('com.first.saccelerator:id/ii').click() 
        self.assertEqual(driver.find_element_by_xpath("//android.widget.Image[@text='14f2fa1a']").text,u'14f2fa1a')
        self.assertEqual(driver.find_element_by_xpath("//android.view.View[@text='￥40 现金券']").text,u'￥40 现金券')
        self.assertEqual(driver.find_element_by_xpath("//android.widget.Image[@text='dcc82ced']").text,u'dcc82ced')
                
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()