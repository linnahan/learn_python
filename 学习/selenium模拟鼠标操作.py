from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
# driver.get(r'D:\gitlearn\learn_python\testlearn\drag.html')
driver.get('https://www.baidu.com/')
driver.maximize_window()

# 实例化鼠标
sb = ActionChains(driver)
# 拖拽移动
# sb.drag_and_drop(driver.find_element_by_id("div1"),driver.find_element_by_id("div2"))
# 悬停
sb.move_to_element(driver.find_element_by_link_text(U'更多'))
# 右键点击
sb.context_click(driver.find_element_by_id("kw"))
# 执行
sb.perform()

sleep(5)
driver.quit()



