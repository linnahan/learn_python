from appium import webdriver
from appium.webdriver.common.touch_action import  TouchAction
from time import sleep


# adb shell dumpsys window | findstr mCurrentFocus  # 获取到app包名和界面名称
# adb shell dumpsys window windows | findstr mFocusedApp
# adb shell getprop ro.build.version.release    #获取手机版本


# 连接移动设备所必须的参数
from selenium.webdriver.common.by import By

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'    # 系统
desired_caps['platformVersion'] = '7.1'      # 系统的版本
desired_caps['deviceName'] = '127.0.0.1:62001'     # 当前要测试的设备的名称
# app 信息
desired_caps['appPackage'] = 'com.android.settings'     # 要启动 app 的名称(包名)
# desired_caps['appPackage'] = 'com.android.launcher3'
# desired_caps['appActivity'] = '.Settings'       # 要启动的 app 的哪个界面
# desired_caps['appActivity'] = '.launcher3.Launcher'
desired_caps['appActivity'] = '.ChooseLockPattern'
# 允许输入中文
desired_caps['unicodeKeyboard'] = True      #unicode 设置(允许中文输入)
desired_caps['resetKeyboard'] = True        #键盘设置(允许中文输入)
# 不重启
# desired_caps['noReset'] = True


# 从 appium 库里面导入 driver 对象
# driver= webdriver.Remomte('appnium 程序的地址','一个字典，要获取设置的要求')
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 2. 执行操作
sleep(2)
# a = driver.find_elements_by_xpath('//*[@text="显示"]')[0]
# a.click()
# 获取信息
# print(a.size)       # 打印大小
# print(a.text)       # 打印属性
# print(a.get_attribute("text"))      # 打印属性
# print(a.location)     # 打印健位置
# print(driver.current_package)   # 打印当前包名
# print(driver.current_activity)  # 打印当前活动页
# print(driver.page_source)       # 打印页源码

# 搜索输入
# driver.find_elements_by_xpath('//*[@content-desc="搜索设置"]')[0].click()
# driver.find_elements_by_xpath('//*[@resource-id="android:id/search_src_text"]')[0].send_keys("123")
# 安装软件包
# driver.install_app(r"C:\Users\admin\Desktop\TPshop.apk")
# if driver.is_app_installed("tv.danmaku.bili"):    #判断删除软件
#     driver.remove_app("tv.danmaku.bili")

# 模拟划动
# el1 = driver.find_element(By.XPATH,"//*[@text = '通知']")
# el2 = driver.find_element(By.XPATH,"//*[@text = 'WLAN']")
# driver.scroll(el1,el2)
# 获取分辨率 540*960
# size = driver.get_window_size()
# width = size['width']
# height = size['height']
# driver.swipe(start_x=width/2,start_y=height/3*2,end_x=width/2,end_y=height/2)
# 拖动
# el1 = driver.find_element(By.XPATH,"//*[@text = '浏览器']")
# el2 = driver.find_element(By.XPATH,"//*[@text = '开发者头条']")
# # driver.drag_and_drop(el1,el2)
# action = TouchAction(driver)
# action.press(el1).wait(3000).move_to(el2)
# action.release()
# action.perform()
# 绘制刷屏手势
# action = TouchAction(driver)
# a, b, x, y = 48, 640, 804, 804
# action.press(x=a+int(x/3*0.5),y=b+int(y/3*0.5)).\
#     wait(500).move_to(x=a+int(x/3*2.5),y=b+int(y/3*0.5)).\
#     wait(500).move_to(x=a+int(x/3*0.5),y=b+int(y/3*2.5)).\
#     wait(500).move_to(x=a+int(x/3*2.5),y=b+int(y/3*2.5))
# action.release()
# action.perform()
# driver.find_element(By.XPATH,'//*[@text="继续"]').click()
# sleep(1)
# action = TouchAction(driver)
# action.press(x=184,y=770).\
#     wait(500).move_to(x=720,y=770).\
#     wait(500).move_to(x=180,y=1310).\
#     wait(500).move_to(x=720,y=1314)
# action.release()
# action.perform()
#其它
# print(driver.network_connection)    #网络信息
# print(driver.device_time)       #手机的时间
# print(driver.get_window_size())     # 分辨率大小
# driver.get_screenshot_as_file("jietu.png")  #截图
# driver.open_notifications() #打开通知栏
# driver.keyevent(2) # 点击按键数字2


# 3. 退出
# driver.close_app()
# driver.quit()
