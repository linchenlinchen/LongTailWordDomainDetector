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
domains = ["zhuandayup.cn", "xaxzhep.com", "whslsz.cn", "zainan.com.cn", "yumijy.cn", "leu17.com", "aaak.top",
           "ynjinlong.cn", "gzkedayiqi.com", "bfdbt.net.cn", "8n3nqq1.buzz", "dafuzhijia.com.cn", "atauscn.cn",
           "xn--1rwm9b515f.cn", "xn--pbt333iujj.cn", "huadiled.com.cn", "zgbaohong.com", "szgasx.cn", "reg30.cn",
           "yunhehd.com", "69nq.cn", "hjgkfl.cn", "5mkskww.buzz", "louisonwoodworks.com", "wztqq.cn", "0t7lpgklny.xyz",
           "lixiangsui.cn", "ai6lc6zblm.xyz", "uz39.com", "fwba3x.cn", "danzhoumutangpingxin.cn", "mbpckbp.cn",
           "82028.com.cn", "hnmjwlkj.cn", "verov.top", "mmwhh.top", "dczkw.cn", "qgltv.top", "tour-market.cn",
           "shandongjinke.top", "violintown.cn", "shanxiangyhq.top", "xinshiwuyou.cn", "ylt58.cn", "evogcckc1s.xyz",
           "zzwjbjfw.cn", "xiaobiesan.top", "xingjitang.com.cn", "jpjboke.top", "xn--ekrq5w1jh.cn", "xinyunde.cn",
           "xuejiejiaoyu.cn", "fsyun.top", "jcjxjzg.cn", "qchen-qc.com", "hhs0906.top", "szhzjz.com", "yvi6pd.cn",
           "casray.club", "zugehao.cc", "unsuq.com", "aceedu.net.cn", "vepx.cn", "ufaljip.cn", "youranplus.cn",
           "xn--p5tw4lnuf.cn", "sqlt.cn", "daishuzhuanqian.cn", "mazhuangxinge.top", "qp84.top", "yangkaihong.cn",
           "wztcb.cn", "gl3vopc4kv.xyz", "lzlongjiang.cn", "ymlmtaz.cn", "youlianjiaoyi.cn", "rhdur61.top", "aad9.cn",
           "zgzszq.com", "xn--qrq020a6tn9oi.cn", "cdbzx.top", "ismile.org.cn", "m7cewh.cn", "yaohong88.cn", "ls64.cn",
           "nhmspkmhg4.xyz", "zgzsmhw.cn", "rimou.top", "jszkfy.cn", "kaibanle.cn", "shangzhongxia.cn",
           "theskateboardschool.com", "xn--qiv838a.cc", "daybuday1.top", "xkgcs.cn", "you100.top", "ychat01.win",
           "yingangxinxizixun.cn", "safebag.org.cn", "ketwy4s5sr.xyz", "anhuika.top", "yqhsdcar.cn", "arconobile.com",
           "miyou1688.com", "hair-welfare.top", "baoqih2.cn", "zsmkswkj.com", "dltwo.top", "greenforesight.cn",
           "9dfgn.cn", "firepointsoft.com.cn", "szcwjs.com", "vv0l4cojdp.xyz", "hkiwc.top", "zhdwg.top", "voii.top",
           "afjrnol.cn", "tuojie.top", "tengneng.cn", "jiaoyimao21.buzz", "6ss.top", "szlbjc.com", "baisongshangjie.cn",
           "incyxwu.cn", "chenyunxin.cn", "cardiffkabel.com.cn", "tuxugn.com", "aivxxt.com", "ledartek.cn", "neif.cn",
           "tdzv.cn", "ziemnmj.cn", "yuandaotax.com", "huazhiqinfs.cn", "77mz.cn", "fatech.online", "87x6eod.buzz",
           "kechenyyp.cn", "changhesteel.cn", "qq9kiwsl9o.xyz", "phmxa5j8jf.xyz", "wvpxyhc.cn", "hycapoj.cn",
           "wdbjz.cn", "huihanzi.com", "sbzyccj.com", "sdpjmedia.cn", "fkxjk.top", "tjwzly.com", "wykl.top", "frpjc.cn",
           "xiaonuomi.com.cn", "hcyuee.top", "aifenxiang88.top", "xn--iiqpw446m.cn", "becstar.cn", "rto4mimdby.xyz",
           "qfjfcty1.cn", "imaofg.top", "hfxfrfdt.cn", "xlwsdp.cn", "ymcvolt.cn", "tppuvhh0ix.xyz", "gxpqmgc.cn",
           "gpufix.top", "buz23qb5.cn", "rifonda.cn", "huaqigj.cn", "jswuye.com.cn", "castlewood.com.cn",
           "chinacowb.com", "yxshhb.com.cn", "4006wosign.com", "mxyxpx.com", "huanhaoinc.com", "cicycat.com",
           "sh-jiejin.com.cn", "ovemlqt.cn", "tuhaowang.cn", "sky58.cn", "zzjdi.top", "amberfans.com.cn", "zajy.com.cn",
           "grand-millennium.cn", "hee0pfl8w4.xyz", "9pmskzn.buzz", "cbgbxyxzx.cn", "acregulator.com.cn", "hdqb267.cn",
           "kukaestrategia.com", "ppneea.cn", "riurl.cn", "btstbj.com", "maxiaoliang.top", "youxigujia.com",
           "sinocrownsd.cn", "letnt7idr9.xyz", "qypw.top", "esastur.com", "mashajihaha.top", "youxucoding.top",
           "firstaidb.top", "web1236.top", "hnweishi.com", "honganonline.cn", "xianhou88.com", "yjyt.net.cn",
           "sl-zhks.top", "gxebfxi.cn", "xn--w2x90pk6p.cn", "fristblood.top", "haitaopai.cn", "hzthealth.com",
           "yypyq.cn", "xxweb.top", "vgbhynv.com", "haogugu.vip", "albuquerquecareerfairs.com", "shandongdingyi.cn",
           "hhinternational.com.cn", "qzbarwx.cn", "88ymxd.top", "jdvsbnt.cn", "henchang.cn", "jtjklm.top",
           "dlrm.com.cn", "m01.com.cn", "tuokeb2b.net", "pssb.top", "xtjlks.cn", "wztca.cn", "sxonekey.cn",
           "jink168.top", "xn--h6q36cd4we1j.cn", "cdjjcz.cn", "aliyun6969.cn", "hpmen.com", "choiceautorepairs.com",
           "fwift.com", "mdoys.cn", "jhkj10.top", "haisheng-dl.com", "zwldmj.top", "qdakdp.cn", "tcfabu.cn",
           "zjz616.com", "shangquan2021.cn", "hljykxsm.cn", "y7o.cn", "shachuangxingcai.com", "teurl.cn", "cnugveq.cn",
           "wttewrc.cn", "aliaviation.com", "xingdongi.com", "eonly.cn", "zycsdhr.top", "liverpoolnewstoday.com",
           "gthjsc.cn", "bonuojiaju.cn", "kepandown.top", "zjhssc.cn", "qtizygf.com.cn", "szmmd.cn", "bievotech.cn",
           "grapewall.cn", "fjlngan.cn", "frbg.cn", "guanshifuwu.com", "uwwhunx.cn", "hzzunhuang.com", "cknhcgzxmv.cn",
           "dmhevuv.cn", "gurumenomori.com", "bxnszs.cn", "shenpinpin.com", "bmhq.cn", "10host.cn", "playwater.com.cn",
           "tytxsj.cn", "ideiadinheiro.com", "blenderkit.cn", "hxwszf.cn", "zion-cn.com", "inxin.com.cn", "mhshwxb.cn",
           "msmzb.com", "utopiaecologica.com", "fy-zm.cn", "cscsw.cn", "hljyww.cn", "gmocso.cn", "aotjo.com",
           "stcmoet.cn", "nyin.top", "wztql.cn", "wglab.cn", "tantuwo.com", "123jl.cn", "sbw1688.com", "shenfux.top",
           "sdhxrs.cn", "54ca.top", "ljzwj.com", "mhhtzl.com", "wlgnjd.com", "baihuowang.com.cn", "avpt.cn",
           "kdpost.top", "1rbrb9.cn", "fengzhiconsulting.com.cn", "577ka.cn", "jinkangzheng.com", "bztchlkj.cn",
           "xn--rhty0to3g5o0byep.cn", "okacomco.com", "qsigdyr.cn", "ghcj.com.cn", "ppyt.cn", "thevoidacademy.com",
           "xmanna.cn", "chenjiagou.top", "skx19980524.top", "moropower.com", "lshcc.com", "qhtongda.cn", "92055.cn",
           "qingjianb.cn", "ttxgy.top", "glkaiyuan.com.cn", "lcnclqy.cn", "hoyu1832.com", "dengyubo.top", "pay722.com",
           "fisnake.cc", "007v.cn", "kmbtva.cn", "cuixiaodong.cn", "longyidao.top", "haiganghld.com",
           "paintcreekproperty.com", "cdtceram.com.cn", "jobonhouse.com", "xn--xhqr21n.net", "wanhezhiyao.cn",
           "gmail2.cn", "zzsaisite.cn"]
domains = ["wlgnjd.com", "baihuowang.com.cn", "avpt.cn",
           "kdpost.top", "1rbrb9.cn", "fengzhiconsulting.com.cn", "577ka.cn", "jinkangzheng.com", "bztchlkj.cn",
           "xn--rhty0to3g5o0byep.cn", "okacomco.com", "qsigdyr.cn", "ghcj.com.cn", "ppyt.cn", "thevoidacademy.com",
           "xmanna.cn", "chenjiagou.top", "skx19980524.top", "moropower.com", "lshcc.com", "qhtongda.cn", "92055.cn",
           "qingjianb.cn", "ttxgy.top", "glkaiyuan.com.cn", "lcnclqy.cn", "hoyu1832.com", "dengyubo.top", "pay722.com",
           "fisnake.cc", "007v.cn", "kmbtva.cn", "cuixiaodong.cn", "longyidao.top", "haiganghld.com",
           "paintcreekproperty.com", "cdtceram.com.cn", "jobonhouse.com", "xn--xhqr21n.net", "wanhezhiyao.cn",
           "gmail2.cn", "zzsaisite.cn"]
with open("new_domains.txt.py",'r') as  f:
    domains = [x.split(",")[0] for x in f.readlines()]
print(domains)
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
        with open("new_domains_tubian.csv", 'a') as f:
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
                    # for title in di.keys():
                    #     try:
                    #         # 打开网站
                    #         driver.set_page_load_timeout(20)
                    #         driver.get(di[title])
                #             # 截取屏幕截图并保存为image.png
                #             time.sleep(0.5)
                #             # name = domain + "-" + title.replace(",", "，").replace(":", "：").replace("/", "") + di[
                #             #     title].replace(",", "，").replace(":", "：").replace("http", "").replace("/", "")
                #             # driver.set_window_size(1920, 1080)
                #             # # driver.save_screenshot(
                #             # #     "/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/reverse_method/pictures/" + name + '.png')
                #             # current_date = datetime.date.today()
                #             # current_month = current_date.month
                #             # current_day = current_date.day
                #             # path = r"/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/pictures_notubian" + "_" + str(
                #             #     current_month) + "_" + str(current_day)
                #             # if not os.path.exists(path):
                #             #     os.mkdir(path)
                #             # driver.save_screenshot(path + "/" + name + '.png')
                #
                        # except:
                        #     print(title + "-" + di[title] + " 404!")
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
