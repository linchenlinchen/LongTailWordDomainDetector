import datetime
import os
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
domains = ["dzzpgs.cn","cxkh.net","ylwhy.org","zhimei168.top","pangaofeng.top","ssjr66.cn","szwekq.com","wangqing15.top","caowensong.top","xmnk.cn","kyun.cn","jsl6.top","hnjcps.com","wushengkai.top","zhjunjia.cn","xylol.top","action2017.top","njjdkt.com","ywj1314.top","nachanghefengjiazheng.cn","wuhantu.top","shqianlx.com","czyxs.cn","zhenggang.net.cn","huyundun.com","nbhsjdz.com","jxlfqc.com","ly-jddz.cn","sqwjj.top","hhllmc.top","hlehuo.com","sixclouds.cn","fhyhy.com","intspire.net","dnovos.com","sdkuma.com","836919126.com","zmserver.top","wwzlxf.top","szyc56.com","tw920.com","ailvgoserver.com","buildtolast.cn","xmd88.cn","52rou.cn","yutenghb.com","t2t.org.cn","dqgqb.net","meituangeek.com","cqqzj.net.cn","wookeer.com","jleh.cn","sufavalve.cn","sxjtzl.com","hfgxkj.cn","xxdntjx.com","covilla.com","xsjxc.com","weldelite.cn","jspyhb.com","srnet.com.cn","monluxe.cn","baoshcn.com","jinguyuan.com.cn","yizhaobiao.net","foremostgroup.com","hfsibokeji.com","lhjtea.com","jkhxdc.com","szsyhs.cn","vis-nicety.cn","hwj123.net","gdzshr.com","jsswj.org.cn","gzluyuan.com","ahyyzn.com","xiulie.top","szstai.com","kingdeepy.com","zhihuiyunying.cn","88sup.com","gyhb666.com","liaokong.com","esscs.cn","zemakeji.com","bhsljt.cn","interhash.top","123jinchan.cn","90hbw.com","chstar.com.cn","lfx668.com","aixinyudz.com","dlunitedmining.com","260cloud.com","hanshangz.com","shssj.net","jsnjdz.com","enjoyvision.cn","yunbokongjian.top","bailianwei.top","jzltzfw.com","dogbk.com","hfcgfc.com","xyfzmy.com","a3v7m2m.top","bjsongzhuang.com.cn","huahaiweb.com","krbova-kamna-krby.com","dplejd.com","weifangfojiao.com","ximengnaikang.com","youhuangou.com","yondoor.com","fkyun.com","aimek.cn","gzqbc.cn","hnjingzun.cn","llzhuan.top","51kuaixue.cn","paidui1.cn","cciccc.com","xlxq66.com","yjlzhj.cn","ycyxf.cn","ephnsgj.cn","kanglietie.com","liujunsh.cn","ceo120.net","quanjingkj.com","pingda56.cn","2chuyou.cn","bc-4.com","sdyudi.cn","xttjnk.com","brelly.com.cn","ncxyb.com","caoqian.top","yxgvojq.cn","fneptft.cn","edsajfl.cn","wkkczxy.cn","itranz.cn","jindouzi123.com","blasoul.com","wxhsc.cn","lzminbai.com.cn","haoyangsoft.com","sdsqzn.com","empress886.com.cn","qfy8.com","jjdhvpz.cn","sangge.top","y8qf.com","vensigpt.com","zhaishiwang.com.cn","pywb.net","lzxf.com.cn","zghuixin.com.cn","cstly.cn","jnoyzia.cn","bbdwr.com","hospitalkowloon.com","buysms.cn","oexlsua.cn","hurstjeepster.com","xilai2017.cn","gwmeeju.cn","dongfengru1.cn","qingshang888888.com.cn","oiuknll.cn","qiyu1018.top","haechi.top","7yzah.cn","upvcu.com","cubbmks.cn","chengjgy.cn","hzfangji.com","feixianw.com","qlcwxrx.cn","shidu168.com","jhsw2014.cn","ewwlzuz.cn","ak561.cn","dijmjke.cn","hlvdhse.cn","disimju.cn","ep37.com","luyitongxun.cn","51sohu.com","8645.com.cn","yuanlinshej.com","ifcxx.com","nltfvop.cn","senkekeji.cn","qvq75z3.cn","gkymljs.cn","gjp9.cn","aemashf.cn","shangnanseo.top","vamqses.cn","uvepvlx.cn","quzhouy.com","scslk.com","cutbqse.cn","lernachowinner.com","shandonghuiyang.com","nt23n.cn","valovfw.cn","sapflvx.cn","tmvppwl.cn","diyiyuesao.cn","zcbgfsh.cn","kmbviak.cn","locnbtz.cn","goivrdp.cn","fjchenfu.com","mjjx168.com","91gwy.net","nvodldk.cn","baidugww.com","fuxgj.cn","z12.cn","shishanzhen.com","edison666.top","sytakad.cn","nrfysmm.cn","sungdo.cc","v36hu2v.cn","xn--44qr78f93b.cn"]
domains = ["fkyun.com","aimek.cn","gzqbc.cn","hnjingzun.cn","llzhuan.top","51kuaixue.cn","paidui1.cn","cciccc.com","xlxq66.com","yjlzhj.cn","ycyxf.cn","ephnsgj.cn","kanglietie.com","liujunsh.cn","ceo120.net","quanjingkj.com","pingda56.cn","2chuyou.cn","bc-4.com","sdyudi.cn","xttjnk.com","brelly.com.cn","ncxyb.com","caoqian.top","yxgvojq.cn","fneptft.cn","edsajfl.cn","wkkczxy.cn","itranz.cn","jindouzi123.com","blasoul.com","wxhsc.cn","lzminbai.com.cn","haoyangsoft.com","sdsqzn.com","empress886.com.cn","qfy8.com","jjdhvpz.cn","sangge.top","y8qf.com","vensigpt.com","zhaishiwang.com.cn","pywb.net","lzxf.com.cn","zghuixin.com.cn","cstly.cn","jnoyzia.cn","bbdwr.com","hospitalkowloon.com","buysms.cn","oexlsua.cn","hurstjeepster.com","xilai2017.cn","gwmeeju.cn","dongfengru1.cn","qingshang888888.com.cn","oiuknll.cn","qiyu1018.top","haechi.top","7yzah.cn","upvcu.com","cubbmks.cn","chengjgy.cn","hzfangji.com","feixianw.com","qlcwxrx.cn","shidu168.com","jhsw2014.cn","ewwlzuz.cn","ak561.cn","dijmjke.cn","hlvdhse.cn","disimju.cn","ep37.com","luyitongxun.cn","51sohu.com","8645.com.cn","yuanlinshej.com","ifcxx.com","nltfvop.cn","senkekeji.cn","qvq75z3.cn","gkymljs.cn","gjp9.cn","aemashf.cn","shangnanseo.top","vamqses.cn","uvepvlx.cn","quzhouy.com","scslk.com","cutbqse.cn","lernachowinner.com","shandonghuiyang.com","nt23n.cn","valovfw.cn","sapflvx.cn","tmvppwl.cn","diyiyuesao.cn","zcbgfsh.cn","kmbviak.cn","locnbtz.cn","goivrdp.cn","fjchenfu.com","mjjx168.com","91gwy.net","nvodldk.cn","baidugww.com","fuxgj.cn","z12.cn","shishanzhen.com","edison666.top","sytakad.cn","nrfysmm.cn","sungdo.cc","v36hu2v.cn","xn--44qr78f93b.cn"]

url = "https://www.baidu.com"


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
        with open("has_tubian.csv", 'a') as f:
            f.write(keyword.split(":")[1] + ",\n")
            for result in results:
                try:
                    title = result.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > h3").text
                    link = result.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(1) > h3 > a").get_attribute(
                        "href")
                    f.write("," + title + "," + link + ",\n")
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
        option.add_argument('-headless')
        # 打开谷歌浏览器
        driver = webdriver.Chrome(options=option)
        # 打开百度搜索主页
        driver.get(url)
        driver.implicitly_wait(5)

        reduce = []
        for domain in domains:
            try:
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
                            name = domain + "-" + title.replace(",", "，").replace(":", "：").replace("/", "") + di[
                                title].replace(",", "，").replace(":", "：").replace("http", "").replace("/", "")
                            driver.set_window_size(1920, 1080)
                            driver.save_screenshot(
                                "/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/reverse_method/pictures/" + name + '.png')
                            current_date = datetime.date.today()
                            current_month = current_date.month
                            current_day = current_date.day
                            path = r"/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/pictures_tubian" + "_" + str(
                                current_month) + "_" + str(current_day)
                            if not os.path.exists(path):
                                os.mkdir(path)
                            driver.save_screenshot(path + "/" + name + '.png')
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


shrink_domain(domains)
