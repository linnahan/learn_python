from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://weibo.com/u/3669102477')
driver.maximize_window()
driver.implicitly_wait(5)

sleep(5)
next = "window.scrollTo(0,10000)"
driver.execute_script(next)
sleep(3)
driver.find_elements_by_xpath('//*[@class="woo-font woo-font--comment toolbar_commentIcon_3o7HB"]')[0].click()
driver.find_elements_by_xpath('//*[@class="woo-box-flex woo-box-alignCenter woo-box-justifyCenter RepostCommentFeed_more_idG8i"]')[0].click()
# driver.find_elements_by_xpath('//*[@class="Comment_toreply_wbBX8 Comment_cursor_2D2XL"]')[0].click()

