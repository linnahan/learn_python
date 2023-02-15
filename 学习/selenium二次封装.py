from selenium.webdriver.support.wait import WebDriverWait



class Base:

    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 截图方法
    # def base_get_img(self):
    #     img_path = DIR_PATH + os.sep + "img" + os.sep + "{}.png".format(time.strftime("%Y%m%d%H%M%S"))
    #     self.driver.get_screenshot_as_file(img_path)

    # 切换frame
    def base_switch_frame(self, loc):
        # 获取元素
        el = self.base_find(loc)
        # 执行切换
        self.driver.switch_to.frame(el)

    # 恢复frame
    def base_default_frame(self):
        self.driver.switch_to.default_content()
