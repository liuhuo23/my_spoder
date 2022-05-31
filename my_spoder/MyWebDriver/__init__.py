import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def jingdong_webdriver():
    browser = webdriver.Chrome()
    browser.get('https://www.jd.com/?cu=true')
    browser.find_element(By.ID, 'key').send_keys("笔记本电脑")
    browser.find_element(By.ID, 'search').find_element(By.TAG_NAME, 'button').click()
    time.sleep(20)
    return browser

if __name__ == '__main__':
    jingdong_webdriver()