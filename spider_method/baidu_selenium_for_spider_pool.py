import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

sys.path.append("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/config")
import re
from util.database.impl.database_impl import add_one_domain_impl
from util.database.impl.database_impl import get_all_domains_info_impl
from util.database.impl.database_impl import db
from util.whois.whois_get_registrant_info import get_whois
from util.database.impl.database_impl import table
from util.code_info_extractor.get_sld_from_url import get_sld


def open_url(url, option):
    # 打开谷歌浏览器
    driver = webdriver.Chrome(options=option)
    # 打开百度搜索主页
    driver.get(url)
    driver.implicitly_wait(9)

    return driver


# 下载网页显示数据
def get_inner_urls(url):
    global title
    inners = set()
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('-headless')
        driver = open_url(url, option)
        try:
            # 加入a标签内的href
            inner_urls = driver.find_elements(By.TAG_NAME, "a")
            for inner_url in inner_urls:
                iu = inner_url.get_attribute("href")
                inners.add(iu)
            # 加入脚本里面的链接
            content = driver.page_source
            pattern = re.compile(
                r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
            urls = re.findall(pattern, content)
            for u in urls:
                inners.add(u)
            # 过滤
            d_s = set()
            special = {";", "；", "'", ")", "\"", "?", ","}
            inners_list = list(inners)
            for inner in inners_list:
                if inner is not None and (
                        "alipay.com" in inner or "baidu.com" in inner or "tencent.com" in inner or "jia.com" in inner):
                    inners.remove(inner)
                    continue
                if inner is not None and "http" in inner and inner != url:
                    n = inner
                    while n[-1] in special:
                        n = n[0:-1]
                    if len(n) < len(inner):
                        inners.add(n)
                        inners.remove(inner)
                else:
                    inners.remove(inner)
            for inner in inners:
                try:
                    if inner.endswith(")") or inner.endswith(".css") or inner.endswith(".gif") or inner.endswith(
                            ".png") or inner.endswith(".jpg") or inner.endswith(".js") or inner.endswith(
                            ".mp3") or inner.endswith(".mp4") or inner.endswith(".avi") or inner.endswith(
                            ".wmv") or inner.endswith(".mpg") or inner.endswith(".mpeg") or inner.endswith(
                            ".mov") or inner.endswith(".swf”") or inner.endswith(".flv") or inner.endswith(
                            ".rm”") or inner.endswith(".ram"):
                        d_s.add(inner)
                except Exception:
                    traceback.print_exc()
                    print("**************" + str(inners))
                    print("&&&&&&&&&&&&&&&&" + str(inner))
            inners.difference_update(d_s)
            # print(inners)
        except Exception as e:
            traceback.print_exc()
        return inners
    except Exception as y:
        traceback.print_exc()
        print(url + " wrong!")
        return set()

def do_spider():
    # 蜘蛛池起点
    # spider_begin = "haoyangsoft.com"
    # table = 'baidu_' + spider_begin + '_result'
    # mongo1 = db.get_mongo()['fraud_detection'][table]
    # domains = {x["url"] for x in mongo1.find()}
    # domains = [x["domain"] for  x in get_all_domains_info_impl(table,"spider")]
    q = {"http://www.haoyangsoft.com/waps.php?FHAl0O.html"}
    # sld集合
    # ds = set()
    # for domain in domains:
    #     domain = domain.split("/")[2]
    #     ds.add(domain)
    # 循环加入新元素
    while len(q) > 0:
        try:
            u = q.pop()
            print("current_url:" + u)
            print("all:" + str(q) + "\n**\n")
            urls = get_inner_urls(u)
            dl = set()
            for i in urls:
                if i is None:
                    continue
                if "php" not in i:
                    dl.add(i)
            urls.difference_update(dl)

            for url in urls:
                # ds.add(url.split("/")[2])
                domain = get_sld(url)
                whois = get_whois(domain)
                if "privacy" in whois['email'].lower():
                    whois['email'] = ""
                if 'privacy' in whois['phone'].lower():
                    whois["phone"] = ""
                if 'privacy' in whois["name"].lower():
                    whois["name"] = ""
                if 'privacy' in whois["org"].lower():
                    whois["org"] = ""
                q.add(url)
                add_one_domain_impl(table, domain, type="spider", check=True, email=whois['email'],
                                    name=whois['name'], phone=whois['phone'], org=whois['org'])
            # if u not in domains and not (inner.endswith(")") or inner.endswith(".css") or inner.endswith(".gif") or inner.endswith(".png") or inner.endswith(".jpg") or inner.endswith(".js") or inner.endswith(".mp3") or inner.endswith(".mp4") or inner.endswith(".avi") or inner.endswith(".wmv") or inner.endswith(".mpg") or inner.endswith(".mpeg") or inner.endswith(".mov") or inner.endswith(".swf”") or inner.endswith(".flv") or inner.endswith(".rm”") or inner.endswith(".ram")):
            #     add_one_word({"url": u})
            if type(urls) == set:
                q = q.union(urls)
                q = list(q)
                mul = set()
                for i in range(len(q)):
                    for j in range(i + 1, len(q)):
                        if get_sld(q[i]) == get_sld(q[j]):
                            mul.add(q[j])
                for n in mul:
                    q.remove(n)
                q = set(q)
            print("____________________________")
        except:
            traceback.print_exc()
            print(":error!")
            print("____________________________")


# do_spider()
