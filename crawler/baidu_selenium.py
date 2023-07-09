from selenium import webdriver
from selenium.webdriver.common.by import By

import random
import time
import sys

sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/")

from config.db import DB
from config.log import Log

# ip = "117.57.98.164:35537"

db = DB()
logger = Log()
table = 'baidu_search_result'
mongo1 = db.get_mongo()['fraud_detection'][table]
words = [x["keyword"] for x in mongo1.find()]
url = "https://www.baidu.com"

def add_one_word(info):
    try:
        mongo1.insert_one(info)
    except Exception as e:
        print("info['word']=" + info['word'] + ":error!")


def open_url(keyword, option):
    # 打开谷歌浏览器
    driver = webdriver.Chrome(chrome_options=option)
    # 打开百度搜索主页
    driver.get(url)
    driver.implicitly_wait(2)
    baidu_put = driver.find_element(By.XPATH, '//*[@id="kw"]')
    baidu_put.send_keys(keyword)
    time.sleep(0.3 + random.random() * 2)
    sech = driver.find_element(By.XPATH, '//*[@id="su"]')
    sech.click()
    return driver


# 下载网页显示数据
def download(keyword):
    global title
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('-headless')
        driver = open_url(keyword, option)

        results1 = driver.find_elements(By.CLASS_NAME, 'result')
        results2 = driver.find_elements(By.CLASS_NAME, 'result-op')
        results = results1 + results2
        d = {}
        count = 0
        for result in results:
            try:
                title = result.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > h3").text
                link = result.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > h3 > a").get_attribute("href")
                print(title)
                print(link)
                d[title] = link
                count += 1
            except Exception as e:
                print(keyword + " " + str(count) + " err!")
        return d
    except Exception as y:
        print(keyword+" wrong!")


if __name__ == "__main__":
    with open('venv/data_bucket/generated_keyword.txt', 'r') as fp:
        while True:
            try:
                keyword = fp.readline()
                print(keyword)
                if keyword in words:
                    continue
                di = download(keyword)
                time.sleep(1 + random.random() * 3)
                if len(di.keys()) < 1:
                    continue
                add_one_word({"keyword": keyword, "info_list": di})
                is_banned = False
                print(keyword + ":OK!")
            except:
                print(keyword+":error!")


