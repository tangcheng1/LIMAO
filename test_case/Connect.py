# coding=utf-8
from appium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ConnectTestLimao(unittest.TestCase):
    def setUp(self):
        desired_caps = {
                    'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'4.4.2',
                    'appPackage':'com.first.saccelerator',
                    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
                    'noReset':True}  
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  #启动
        self.driver.implicitly_wait(10)       
        
    def test_Connect(self):
        driver = self.driver
        try:            
            driver.find_element_by_id('com.first.saccelerator:id/ij').click() #点击升级  
        except:  
            print('f')
        try:            
            driver.find_element_by_id('com.first.saccelerator:id/ni').click() #点击升级  
        except:  
            print('f')
        try:     
            driver.find_element_by_id('com.first.saccelerator:id/nf').click() #点击公告
        except:  
            print('f')
        try:  
            driver.find_element_by_id('com.first.saccelerator:id/nf').click() #点击公告  
        except:  
            print('f') 
        driver.find_element_by_id('com.first.saccelerator:id/gr').click()  #点击连接          
        WebDriverWait(driver, 10, 0.5).until(EC.text_to_be_present_in_element((By.ID,'com.first.saccelerator:id/gt'), u'点击断开'))
        self.assertEqual(driver.find_element_by_id('com.first.saccelerator:id/gt').text,u'点击断开')
     
#         driver.keyevent(3)    #home到桌面    
# #         driver.press_keycode(3)
#         driver.start_activity('com.android.chrome','com.google.android.apps.chrome.Main')     #打开chrome浏览器
#         driver.find_element_by_id('com.android.chrome:id/url_bar').clear()                 #清除URL 
#         driver.find_element_by_id('com.android.chrome:id/url_bar').send_keys('https://www.youtube.com')  #输入url
#         driver.keyevent(66)  #确认回车
# #         driver.press_keycode(66)
# 
#         self.assertEqual(driver.find_element_by_id('com.android.chrome:id/url_bar').text,u'https://m.youtube.com')
#         self.assertEqual(driver.find_element_by_xpath('//android.view.View/android.view.View[2]').text,u'首页')
    
    def tearDown(self):
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main()
    
    
