# coding=utf-8
from appium import webdriver
import unittest
class LoginTestLimao(unittest.TestCase):
    def setUp(self):
        desired_caps = {
                    'platformName':'Android',
                    'deviceName':'127.0.0.1:62001',
                    'platformVersion':'4.4.2',
                    'appPackage':'com.first.saccelerator',
                    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
                    'noReset':True}  
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        self.driver.implicitly_wait(10)                                
    def test_login(self):
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
        #进入首页后点击‘我的’按钮
        driver.find_element_by_id('com.first.saccelerator:id/gf').click()    
        # 点击登录头像按钮，进行登录，跳转到登录界面
        driver.find_element_by_id('com.first.saccelerator:id/lv').click() 
        # 输入用户名
        driver.find_element_by_id('com.first.saccelerator:id/fy').clear()
        driver.find_element_by_id('com.first.saccelerator:id/fy').send_keys('18702766541')
        driver.hide_keyboard()  #隐藏输入法
        driver.find_element_by_id('com.first.saccelerator:id/g1').clear()
        # 输入密码
        driver.find_element_by_id('com.first.saccelerator:id/g1').send_keys('654321')
        driver.hide_keyboard() #隐藏输入法
        # 点击确认登录按钮
        driver.find_element_by_id('com.first.saccelerator:id/g2').click()                    
        # 进入首页后点击‘我的’按钮
        driver.find_element_by_id('com.first.saccelerator:id/gf').click()
        # 添加断言
        self.assertEqual(driver.find_element_by_id('com.first.saccelerator:id/kw').text,u'18702766541')
 
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()