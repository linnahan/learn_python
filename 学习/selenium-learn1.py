from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()
driver.get(r"D:\gitlearn\learn_python\testlearn\注册A.html")
# driver.get("https://www.toutiao.com")
driver.implicitly_wait(5)
driver.maximize_window()

#键盘操作
# user_ele = driver.find_element_by_id('userA')
# user_ele.send_keys('雷神')
# user_ele.send_keys(Keys.CONTROL,'a')
# sleep(2)
# user_ele.send_keys(Keys.CONTROL,'c')
# user_ele.send_keys(Keys.BACKSPACE)
# user_ele.send_keys(Keys.CONTROL,'v')

# 下拉框选择
# sele = Select(driver.find_element_by_id('selectA'))
# # 通过下标选择
# sele.select_by_index(1)
# # 通过值value选择
# sele.select_by_value("gz")
# # 通过显示文本选择
# sele.select_by_visible_text("A重庆")

# 滚动
# sleep(3)
# sc = "window.scrollTo(0,10000)"
# driver.execute_script(sc)

# 警告框
driver.find_element_by_id("alerta").click()
alerta = driver.switch_to.alert
sleep(2)
# 打印警告
print(alerta.text)
# 接受警告
# alerta.accept()
# 拒接警告
alerta.dismiss()


sleep(5)
driver.quit()


