import traceback

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


# 下载网页显示数据
def download(driver, keyword):
    global title
    try:
        baidu_put = driver.find_element(By.XPATH, '//*[@id="kw"]')
        baidu_put.send_keys(keyword)
        time.sleep(0.3 + random.random() * 2)
        sech = driver.find_element(By.XPATH, '//*[@id="su"]')
        sech.click()
        results1 = driver.find_elements(By.CLASS_NAME, 'result')
        # results2 = driver.find_elements(By.CLASS_NAME, 'result-op')
        results = results1
        # if results '深度合作\n百度信誉V 开放平台 官网认证\n百度开放计划，让搜索引擎发现您的价值'
        d = {}
        count = 0
        print(results)
        for result in results:
            try:
                title = result.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > h3").text
                link = result.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > h3 > a").get_attribute(
                    "href")
                print(title, end="\t")
                print(link)
                d[title] = link
                count += 1
            except Exception as e:
                print(keyword + " " + str(count) + " err!")
        return d
    except Exception as y:
        traceback.print_exc()
        return {}


def shrink_domain(domains):
    try:
        option = webdriver.ChromeOptions()
        # option.add_argument('-headless')
        # 打开谷歌浏览器
        driver = webdriver.Chrome(options=option)
        # 打开百度搜索主页
        driver.get(url)
        driver.implicitly_wait(5)

        reduce = []
        for domain in domains:
            try:
                # di = set_timeout(download,[driver, "site:" + domain], timeout=10)
                di = download(driver, "site:" + domain)
                time.sleep(1 + random.random() * 3)
                if len(di.keys()) < 1:
                    reduce.append(domain)
                    driver.get(url)
                    continue
                else:
                    # 对内容进行检查
                    for title in di.keys():
                        try:
                            # 打开网站
                            driver.set_page_load_timeout(20)
                            driver.get(di[title])
                            # 截取屏幕截图并保存为image.png
                            time.sleep(2)
                            name = domain + "-"+title.replace(",", "，").replace(":", "：").replace("/", "")+di[title].replace(",", "，").replace(":", "：").replace("http", "").replace("/","")
                            driver.save_screenshot("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/reverse_method/pictures/" + name + '.png')

                        except:
                            print(title + "-" + di[title] + " 404!")
                    driver.get(url)
            except:
                # traceback.print_exc()
                print(domain + " 404!")
        # 关闭WebDriver实例
        driver.quit()
        return reduce
    except:
        traceback.print_exc()

