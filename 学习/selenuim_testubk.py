from selenium import webdriver
from time import sleep

browers = webdriver.Chrome()
browers.implicitly_wait(3)

def login_back():
    browers.get("https://dev.bnzedu.com/admin/#/login")
    browers.maximize_window()
    browers.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/span/span/input').send_keys(1640936424877)
    browers.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/span/span/input').send_keys(123456)
    browers.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/div/span/button').click()

def add_class():
    browers.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/aside/div/ul/li[3]/div/span/span').click()
    browers.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/aside/div/ul/li[3]/ul/li[1]/a').click()
    browers.find_element_by_xpath('//*[@id="components-layout-demo-custom-trigger"]/section/main/div/div[1]/div/button').click()
    browers.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/span/input').send_keys("啊啊啊")
    browers.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()



if __name__ == '__main__':
    login_back() # 登录后台
    add_class() #增加分类
    sleep(10)
    browers.quit()