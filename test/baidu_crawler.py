import random
import time
import traceback

import requests
from bs4 import BeautifulSoup
import sys

def get_baidu_search_result(keyword, ip):
    try:
        proxies = {
            "http": "" + ip,
            "https": "" +  ip
        }
        print(proxies)
        url = 'https://www.baidu.com/s'
        params = {'wd': keyword}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            "Cookie": "PSTM=1660833817; BAIDUID=2721832B494F290028AC71DEC18B8501:FG=1; BIDUPSID=5078DA522A80F23B94D84796223ABB65; BD_UPN=123253; H_PS_PSSID=36558_38470_38440_38309_38468_38289_36804_38486_37931_38382_38356_26350_22159_37881; BA_HECTOR=8k0h0lal24810ha58k218gcu1i2l65u1n; BAIDUID_BFESS=2721832B494F290028AC71DEC18B8501:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=naVXOxGfri0BT8LPcAZN0x3BRxlouk:BniTISbfb3Z8c:C; SL_G_WPT_TO=zh; BD_CK_SAM=1; PSINO=1; delPer=0; COOKIE_SESSION=456_0_9_9_5_23_0_0_8_9_1_5_10390_0_0_0_1680253741_0_1680513670|9#351105_45_1679424425|9; ab_sr=1.0.1_YmVjNjMxZjdlMTIyOWUwNTdjMGIwMTJhMTY3MjEzNDVmN2ZhZTM5MDAzZjg3MWYzNGM2MDM5NDhiMGRjZmM5OWYwOTIyMDQ4YTgzMTg2ODI1NmU3Zjg4NGUxOTdiYjA4ZjczNWVmY2EyZWI3NGFiYWQwZGQ4NWVjNjI4MTQyOTY5ZmYzNDE0YzQ3NTU4N2FjNWU2OGUyZWEzN2IzZGQ3NA==; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; H_PS_645EC=ea39y/F/aVwkp2xlVkEB5C7Z5ykV9HRi886WunDPyaxLuWmZcKHZcL0NAAs"
        }
        # 常见的 user-agent 列表
        headers_list = [
            {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
            }, {
                'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
            }, {
                'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
            }, {
                'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
            }, {
                'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
            }, {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
            }, {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
            }, {
                'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
            }
        ]
        headers = random.choice(headers_list)
        response = requests.get(url, params=params, headers=headers, proxies=proxies, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='result')
        # results += soup.find_all('div', class_='result-op')
        di = {}
        for result in results:
            try:
                title = result.h3.text
                print(title)
                di[title] = "ing"
            except Exception as e:
                traceback.print_exc()
    except:
        traceback.print_exc()
        time.sleep(5)
        return get_baidu_search_result(keyword, ip)
    return di


def error_log(word):
    print(" none!")
    with open("venv/data_bucket/err.txt", 'a') as e:
        e.write(word)


def get_ip():
    try:
        u = "http://http.tiqu.letecs.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
        # print(u)
        ip = requests.get(u)
        # print(ip.text)
    except:
        traceback.print_exc()
        return ""
    return ip.text.split("\r\n")[0]


import datetime

if __name__ == '__main__':
    is_banned = False
    count = 0
    starttime = datetime.datetime.now()
    # time.sleep(10)
    ip = get_ip()
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
    with open("no_tubian.csv", 'a') as f:
        for domain in domains:
            try:
                endtime = datetime.datetime.now()
                print(str(endtime) + "," + str(starttime) + str((endtime - starttime).seconds))
                if (endtime - starttime).seconds >= 8:
                    ip = get_ip()
                    print(ip)
                    starttime = endtime
                di = get_baidu_search_result("site:"+domain, ip)
                print(di)

                # f.write(domain + ",\n")
                for result in di.keys():
                    f.write(result)
            except:
                traceback.print_exc()
