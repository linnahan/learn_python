from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(50)
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("性感美女")
driver.find_element_by_id("su").click()
driver.find_elements_by_xpath('//*[@class="image-two-line_1_lXw"]/a/img')[1].click() # 选一张图片
print(driver.window_handles) # 打印全部句柄
print(driver.current_window_handle) # 当前句柄
driver.switch_to.window(driver.window_handles[1]) # 操作进入第二个窗口
driver.find_element_by_id('currentImg').click() # 点击进入图片源地址
driver.switch_to.window(driver.window_handles[2]) # 操作进入第三个窗口
driver.switch_to.window(driver.window_handles[0]) # 操作进入第三个窗口
print(driver.current_window_handle)
print(driver.window_handles)
driver.save_screenshot('meinv.png') # 保存图片

