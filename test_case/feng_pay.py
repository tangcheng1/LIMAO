# coding=utf-8
import unittest
from appium import webdriver
import BasePage
import  ConfigParser
 
class BaiduSearch(unittest.TestCase):
    def setUp(self):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'  
#         desired_caps['platformVersion'] = '6.0.1' 
#         desired_caps['deviceName'] = '59eadad3'  
#         desired_caps['appPackage'] = 'com.first.saccelerator'  
#         desired_caps['appActivity'] = 'com.first.saccelerator.ui.activity.CheckPermissionsActivity'  
#         desired_caps['noReset'] = True  
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  
#         self.driver.implicitly_wait(10)
#         self.driver = BasePage.Base().get_driver()  
        
        BasePage.Base().kaiji()#开机过广告
        
    def test_Pay(self):
        row=BasePage.Base().mysql('SELECT current_coins FROM users WHERE id = 588')#数据库取结果
        BasePage.Base().pay()#支付
        row1=BasePage.Base().mysql('SELECT current_coins FROM users WHERE id = 588') #数据库再取结果
          
#         cfg = ConfigParser.SafeConfigParser()    
#         cfg.read('E:/eclipse-workspace/LIMAO/config.ini')
#         driver=self.driver
#         try:  
#             driver.find_element_by_id(cfg.get('Login', 'Ad1')).click() #点击开屏广告
#         except:
#             print('开f')
#         try:  
#             driver.find_element_by_id(cfg.get('Login','Ad2')).click() #点击开机广告
#         except:
#             print('f')
#         try:
#             driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击升级
#         except:
#             print('f')
#         try:
#             driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击公告
#         except:
#             print('f')
#         driver.find_element_by_id(cfg.get('Login','Recharge')).click()  
#         driver.find_element_by_id(cfg.get('Login','buy')).click()         
#         driver.find_element_by_xpath("//android.widget.Button[@text='确认支付']").click()  
#         driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()  
        
#         connection = pymysql.connect(host='120.79.61.217', port=3306, user='svpn', password='wfzc3vUJjy8hhO{', db='svpn', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#         cursor = connection.cursor()#建立游标       
#         sql = 'SELECT current_coins FROM users WHERE id = 587'
#         cursor.execute(sql)
#         result1 = cursor.fetchone()
#         for row1 in result1.values():
#             print(row1)
        self.assertEqual(row1,row+15)
        
    def tearDown(self):
#         self.driver.quit()
        BasePage.Base().quit()
  
 
if __name__ == "__main__":
    unittest.main()