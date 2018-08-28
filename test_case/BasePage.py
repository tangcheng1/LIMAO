#coding=utf-8
import pymysql.cursors
import  ConfigParser
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,os

class Base(object):
    cfg = ConfigParser.SafeConfigParser()    
    cfg.read('E:/eclipse-workspace/LIMAO/config.ini') 
    desired_caps = {
                    'platformName':'Android',
                    'deviceName':cfg.get('DEFAULT', 'devices'),
                    'platformVersion':cfg.get('DEFAULT', 'platformVersion'),
                    'appPackage':'com.first.saccelerator',
                    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
                    'noReset':True} 
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30) 
    def get_driver(self):
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
        return self.driver       

    def mysql(self,sql):
        connection = pymysql.connect(host='120.79.61.217', port=3306, user='svpn', password='wfzc3vUJjy8hhO{', db='svpn', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
#         sql = 'SELECT current_coins FROM users WHERE id = 587'
        cursor.execute(sql)
        result =cursor.fetchone()
        for row in result.values(): #获取values
            return(row)
        connection.close()#关闭数据 
        
    def kaiji(self):
        driver = self.driver  
        cfg = ConfigParser.SafeConfigParser()  
        cfg.read('E:/eclipse-workspace/LIMAO/config.ini')
        try:  
            driver.find_element_by_id(cfg.get('Login', 'Ad1')).click() #点击开屏广告
        except:
            print('开f')
        try:  
            driver.find_element_by_id(cfg.get('Login','Ad2')).click() #点击开机广告
        except:
            print('f')
        try:
            driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击升级
        except:
            print('f')
        try:
            driver.find_element_by_id(cfg.get('Login','Notice')).click() #点击公告
        except:
            print('f')    
    def pay(self): 
        driver = self.driver
        cfg = ConfigParser.SafeConfigParser()  
        cfg.read('E:/eclipse-workspace/LIMAO/config.ini')
        driver.find_element_by_id(cfg.get('Login','Recharge')).click()  
        driver.find_element_by_id(cfg.get('Login','buy')).click()         
        driver.find_element_by_xpath("//android.widget.Button[@text='确认支付']").click()  
        driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click() 
    def quit(self):
        driver = self.driver
        driver.quit()
           
    def login(self):
        driver = self.driver
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

