from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(50)
driver.get("https://www.baidu.com")
driver.add_cookie({'name':"BDUSS","value":"REbklDaTVTSTA3LXZUeGpwQzlKM3ByOWNRdkhhVi1VTTRVQUVufjlMNmZjZ0JrSVFBQUFBJCQAAAAAAAAAAAEAAAC1jtw5use6x7n-sKFzbWlsZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ~l2GOf5dhjZF"})
driver.add_cookie({'name':"BAIDUID","value":"8C0BD16C3A21164A985CFB3C9BC07682:FG=1"})
sleep(3)
driver.refresh()
sleep(5)
driver.quit()