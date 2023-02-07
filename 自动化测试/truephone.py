from appium import webdriver
from time import sleep


# adb shell dumpsys window | findstr mCurrentFocus  # 获取到app包名和界面名称
# adb shell dumpsys window windows | findstr mFocusedApp
# adb shell getprop ro.build.version.release    #获取手机版本


# 连接移动设备所必须的参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'    # 系统
desired_caps['platformVersion'] = '12'      # 系统的版本
desired_caps['deviceName'] = 'FM7TX8IB55AY6THI'     # 当前要测试的设备的名称
# app 信息
desired_caps['appPackage'] = 'com.tencent.mm'     # 要启动 app 的名称(包名)
desired_caps['appActivity'] = '.ui.LauncherUI'       # 要启动的 app 的哪个界面
# 允许输入中文
desired_caps['unicodeKeyboard'] = True      #unicode 设置(允许中文输入)
desired_caps['resetKeyboard'] = True        #键盘设置(允许中文输入)
# 不重启
desired_caps['noReset'] = True


# 从 appium 库里面导入 driver 对象
# driver= webdriver.Remomte('appnium 程序的地址','一个字典，要获取设置的要求')
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 2. 执行操作
# driver.xxx
sleep(2)
print(driver.page_source)
driver.find_element_by_xpath("//*[text()='祝文杰']") .click()

# element = driver.find_element_by_xx()   # element.xxx

# 3. 退出
# driver.close_app()
driver.quit()
