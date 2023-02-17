from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_base import Base

driver = webdriver.Chrome()
driver.maximize_window()
dd = Base(driver)
driver.get('https://book.qidian.com/info/1036135529/#Catalog')
tt = dd.base_get_text((By.XPATH,'//div[@class="book-info "]/h1/em'))
print(tt)
zj = dd.base_findall((By.XPATH,'//*[@id="j-catalogWrap"]/div/div/ul/li/h2/a'))
for i in zj:
    print(i.text + i.get_attribute('href'))
driver.quit()
