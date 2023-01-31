from selenium import webdriver
from time import sleep



def openWeb():
    brower.get("http://www.kulemi.com/content/457393/")
    brower.maximize_window()

def getTitle():
    xpth0 = '//*[@class="chapter-head"]/h2'
    title = brower.find_elements_by_xpath(xpth0)[0].text
    print(title)

def getBody():
    xpth1 = '//*[@class="chapter-content"]/p'
    body_ele = brower.find_elements_by_xpath(xpth1)
    for i in body_ele:
        print(i.text)

def next():
    brower.find_elements_by_xpath('//*[@id="chapterNext"]/i')[0].click()

if __name__ == '__main__':
    brower = webdriver.Chrome()
    openWeb()
    for i in range(3):
        getTitle()
        getBody()
        print('''
        
        ''')
        next()
        sleep(1)
    brower.quit()