from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://mail.qq.com")

# 切框frame
driver.switch_to.frame("login_frame")
# 输入账号
driver.find_element_by_id("u").send_keys(145213315)
# 切换回原框架
driver.switch_to.default_content()
print(driver.find_elements_by_xpath('/html/body/div/div[1]/a')[0].text)