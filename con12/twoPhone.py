#coding=utf-8
from appium import webdriver
import time
import threading
desired_caps = {
    'platformName':'Android',  # 设备系统平台
    'deviceName':'127.0.0.1:62001',#设备名称
    'platformVersion':'4.4.2',#设备系统版本
    'appPackage':'com.first.saccelerator',# 测试app包名
    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',#测试appActivity
    'noReset':True #如果没有回从安装后的界面开始
}
desired_caps2 = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62025',
    'platformVersion':'5.1.1',
    'appPackage':'com.first.saccelerator',
    'appActivity':'com.first.saccelerator.ui.activity.CheckPermissionsActivity',
    'noReset':True
}
def task1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  
    driver.implicitly_wait(10) 
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
def task2():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    driver.implicitly_wait(10) 
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
threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)

t2 = threading.Thread(target=task2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()