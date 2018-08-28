# coding=utf-8
from appium import webdriver
import unittest
import pymysql.cursors
import  ConfigParser


class ConnectTestLimao(unittest.TestCase):
    
    
    def setUp(self):
        cfg = ConfigParser.SafeConfigParser()    
        cfg.read('E:/eclipse-workspace/LIMAO/config.ini') 
        desired_caps = {
                    'platformName':'Android',
                    'deviceName':cfg.get('DEFAULT', 'devices'),
                    'platformVersion':cfg.get('DEFAULT', 'platformVersion'),
                    'appPackage':'com.first.saccelerator',
                    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
                    'noReset':True}  
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        
                      
    def test_Pay(self):
        connection = pymysql.connect(host='120.79.61.217', port=3306, user='svpn', password='wfzc3vUJjy8hhO{', db='svpn', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()#建立游标
        sql = 'SELECT current_coins FROM users WHERE id = 588'
        cursor.execute(sql)#使用execute方法执行SQL语句
        result =cursor.fetchone()#运行sql结果 
        for row in result.values(): #获取values
            print(row)
        connection.close()#关闭数据库
        driver = self.driver
        cfg = ConfigParser.SafeConfigParser()    
        cfg.read('E:/eclipse-workspace/LIMAO/config.ini')             
        try:  
            driver.find_element_by_id(cfg.get('Login', 'Ad1')).click() #点击升级 
        except:
            print('f')
        try:  
            driver.find_element_by_id(cfg.get('Login','Ad2')).click() #点击升级
        except:
            print('f')
        try:
            driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击升级
        except:
            print('f')
        try:
            driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击升级
        except:
            print('f')
        driver.find_element_by_id(cfg.get('Login','Recharge')).click()  
        driver.find_element_by_id(cfg.get('Login','buy')).click()         
        driver.find_element_by_xpath("//android.widget.Button[@text='确认支付']").click()  
        driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click() 
        #调用数据库  
        connection = pymysql.connect(host='120.79.61.217', port=3306, user='svpn', password='wfzc3vUJjy8hhO{', db='svpn', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()#建立游标       
        sql = 'SELECT current_coins FROM users WHERE id = 588'
        cursor.execute(sql)
        result1 = cursor.fetchone() 
        for row1 in result1.values():
            print(row1)
        connection.close()#关闭数据库
        
        self.assertEqual(row1,row+15)
        
        
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == "__main__":
    unittest.main()
    