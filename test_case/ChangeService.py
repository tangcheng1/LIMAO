# coding=utf-8
from appium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import BasePage

class ServiceTestlimao(unittest.TestCase):
    def setUp(self):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'  # 设备系统
#         desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
#         desired_caps['deviceName'] = '127.0.0.1:62001'  # 设备名称
#         desired_caps['appPackage'] = 'com.first.saccelerator'  # 测试app包名
#         desired_caps['appActivity'] = 'com.first.saccelerator.ui.activity.CheckPermissionsActivity'  # 测试appActivity
#         desired_caps['noReset'] = True  
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app        
#         self.driver.implicitly_wait(10) 
        self.driver = BasePage.Base().get_driver()  
        
    def test_ChangeService(self):
        driver = self.driver    
        try:            
            driver.find_element_by_id('com.first.saccelerator:id/ij').click() #点击广告
        except:  
            print('f')
        try:            
            driver.find_element_by_id('com.first.saccelerator:id/ni').click() #点击广告 
        except:  
            print('f')
        try:     
            driver.find_element_by_id('com.first.saccelerator:id/nf').click() #点击升级  
        except:  
            print('f')
        try:  
            driver.find_element_by_id('com.first.saccelerator:id/nf').click() #点击公告  
        except:  
            print('f') 
        driver = self.driver 
      
        # 进入首页后点击‘精英服务’按钮
        if  driver.find_elements_by_android_uiautomator('new UiSelector().text("王者服务")'):
            driver.find_elements_by_android_uiautomator('new UiSelector().text("王者服务")')[0].click()
            WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id("com.first.saccelerator:id/n0"))
#             DashPage.Element().swipe_to_left() 
            width=driver.get_window_size()['width']#另一种左滑的方式
            height=driver.get_window_size()['height']
            driver.swipe(width/2,height*7/8,width/10,height*7/8,400)
            driver.find_element_by_id('com.first.saccelerator:id/jv').click()
            WebDriverWait(driver, 10, 0.5).until(EC.text_to_be_present_in_element((By.ID,'com.first.saccelerator:id/gt'), u'点击断开'))
            self.assertEqual( driver.find_element_by_id('com.first.saccelerator:id/gv').text,u'精英服务')
            self.assertEqual( driver.find_element_by_id('com.first.saccelerator:id/gt').text,u'点击断开') 
            
        elif driver.find_elements_by_android_uiautomator('new UiSelector().text("精英服务")'):
            driver.find_elements_by_android_uiautomator('new UiSelector().text("精英服务")')[0].click() 
            WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_id("com.first.saccelerator:id/n0"))
            # driver.swipe(720, 1495, 121, 1495,600) #一种左滑动方式
            width=driver.get_window_size()['width']#另一种左滑的方式
            height=driver.get_window_size()['height']
            driver.swipe(width/2,height*7/8,width/10,height*7/8,400)
            driver.find_element_by_id('com.first.saccelerator:id/jv').click()
            WebDriverWait(driver, 10, 0.5).until(EC.text_to_be_present_in_element((By.ID,'com.first.saccelerator:id/gt'), u'点击断开'))
            self.assertEqual( driver.find_element_by_id('com.first.saccelerator:id/gv').text,u'王者服务')
            self.assertEqual( driver.find_element_by_id('com.first.saccelerator:id/gt').text,u'点击断开')
        else:
            print('f')
  
    def tearDown(self):
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main()