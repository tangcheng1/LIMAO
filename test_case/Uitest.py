# coding=utf-8
from appium import webdriver
import unittest
import  ConfigParser
import BasePage
class UITestlimao(unittest.TestCase):

    def setUp(self):
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub',BasePage.Base.desired_caps)  # 启动app
#         self.driver.implicitly_wait(10)
        self.driver = BasePage.Base().get_driver()     
    def test_ui(self):  
        driver=self.driver        
        cfg = ConfigParser.SafeConfigParser()    
        cfg.read('E:/eclipse-workspace/LIMAO/config.ini')           
        try:  
            driver.find_element_by_id(cfg.get('Login', 'Ad1')).click() #点击升级 
        except:
            print('f')
        driver.find_element_by_id(cfg.get('Login','Ad2')).click() #点击升级
        driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击升级     
        driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击升级  
        self.assertEqual(driver.find_element_by_id(cfg.get('Login','me')).text,u'我的')
        
    def tearDown(self):
        self.driver.quit() 
if __name__ == "__main__":
    unittest.main()