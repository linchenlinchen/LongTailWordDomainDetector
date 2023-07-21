import random
import time

from selenium.webdriver.common.by import By

from spider_method.baidu_selenium_for_spider_pool import open_url
from selenium import webdriver



url = "https://www.baidu.com"
option = webdriver.ChromeOptions()
# option.add_argument('-headless')
driver = open_url(url, option)
with open("draft.txt", 'r') as f:
    flag = True
    i= 0
    while flag:
        i += 1
        line = f.readline().split("\t")[0]
        if i < 153:
            continue
        baidu_put = driver.find_element(By.XPATH, '//*[@id="kw"]')
        baidu_put.send_keys("site:"+line)
        time.sleep(0.3 + random.random() * 2)
        sech = driver.find_element(By.XPATH, '//*[@id="su"]')
        sech.click()

        # 打开新的标签页
        js = 'window.open("https://www.baidu.com");'
        driver.execute_script(js)
        time.sleep(1)
        handles = driver.window_handles
        driver.switch_to.window(handles[len(handles)-1])
        if len(line)<= 1:
            flag = False
        print(line)
while True:
    time.sleep(10000)