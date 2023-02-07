from appium import webdriver
from appium.webdriver.common.touch_action import  TouchAction
from time import sleep

from selenium.webdriver.common.by import By

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'    # 系统
desired_caps['platformVersion'] = '7.1'      # 系统的版本
desired_caps['deviceName'] = '127.0.0.1:62001'     # 当前要测试的设备的名称
# 允许输入中文
desired_caps['unicodeKeyboard'] = True      #unicode 设置(允许中文输入)
desired_caps['resetKeyboard'] = True        #键盘设置(允许中文输入)
desired_caps['appPackage'] = 'com.tpshop.malls'  # 要启动 app 的名称(包名)
desired_caps['appActivity'] = '.SPMainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(2)

def login():
    driver.find_element(By.XPATH, "//*[@text='我的']").click()
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/head_img']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/mobile_et']").send_keys('13600000012')
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/pwd_et']").send_keys('123456')
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/agree_btn']").click()
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/login_tv']").click()

def buy():
    driver.find_element(By.XPATH,"//*[@text='输入你想要搜索的内容']").click()
    sleep(1)
    driver.find_element(By.XPATH,"//*[@text='请输入要搜索的商品']").send_keys('小米12')
    driver.find_element(By.XPATH,"//*[@text='搜索']").click()
    sleep(1)
    action = TouchAction(driver)
    action.press(x=250,y=430).wait(300)
    action.release()
    action.perform()
    sleep(3)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/promptly_buy_tv']").click()    #购买
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/confirm_tv']").click() #确定
    sleep(0.5)
    # 登录
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/mobile_et']").send_keys('13600000012')
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/pwd_et']").send_keys('123456')
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/agree_btn']").click()
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/login_tv']").click()
    sleep(2)

    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/confirm_tv']").click()  # 确定
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/submit_tv']").click() # 提交订单
    sleep(1)
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/pay_btn']").click()  # 支付
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/pwd_et']").send_keys('123456')
    driver.find_element(By.XPATH, "//*[@resource-id='com.tpshop.malls:id/sure_tv']").click()

if __name__ == '__main__':
    # login()
    buy()