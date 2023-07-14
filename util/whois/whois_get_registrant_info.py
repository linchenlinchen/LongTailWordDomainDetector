import os
import sys
import re
import codecs
import chardet
import openpyxl
import requests


from bs4 import BeautifulSoup

import codecs
import csv
import sys
import traceback
from util.datetime.is_future import is_time_after_current
sys.path.append("/config/")


sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/reverse_method")
from config.db import DB
from config.log import Log

def query_filtered_whois_detail(domain):
    info = query_whois_detail(domain)
    # print(info)
    try:
        if info is None:
            return None
        if "registrantEmail" not in info.keys():
            info["registrantEmail"] = [""]
        if "registrantOrganization" not in info.keys():
            info["registrantOrganization"] = [""]
        if "registrantName" not in info.keys():
            info["registrantName"] = [""]
        if "registrantTelephone" not in info.keys():
            info["registrantTelephone"] = [""]

        if "@" not in info["registrantEmail"][0] or "privacy" in info["registrantEmail"][0].lower():
            info["registrantEmail"][0] = ""
        if 'privacy' in info["registrantOrganization"][0].lower():
            info["registrantOrganization"][0] = ""
        if 'privacy' in info["registrantName"][0].lower():
            info["registrantOrganization"][0] = ""
        if 'privacy' in info["registrantTelephone"][0].lower():
            info["registrantTelephone"][0] = ""
    except:
        traceback.print_exc()
    return info

def query_whois_detail(domain):
    headers = {
        'Connection': 'close',
        'fdp-access': 'c2ae6e5e6c914c54adad68caf6c55b2e',
        'fdp-secret': 'ekzPK2j+BiFp/ZOZ/Izz+pmsWAB/qdqPKNR2lUoAb6lDqndRtbocK6iDLqeK3XvTfYNASHlF5VUjDOunifYTYOIoc8XvCTCIak3XV0ZxprJALyuban4+gPA+Mhwj/vLM'
    }
    proxy = "tp.a0ab.com:25517"
    proxies = {
        "https": "https://{0}".format(proxy),
        "http": "http://{0}".format(proxy),
    }
    params = {
        'merge': 0 # 0 合并, 1 返回注册局, 2 返回注册商
    }
    url = f'http://fdp.qianxin-inc.cn/v3/whois/detail/{domain}'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)

    if "data" in response.json().keys():
        return response.json()['data']
    return None


def query_whois_by_email(email, need_active):
    headers = {
        'Connection': 'close',
        'fdp-access': 'c2ae6e5e6c914c54adad68caf6c55b2e',
        'fdp-secret': 'ekzPK2j+BiFp/ZOZ/Izz+pmsWAB/qdqPKNR2lUoAb6lDqndRtbocK6iDLqeK3XvTfYNASHlF5VUjDOunifYTYOIoc8XvCTCIak3XV0ZxprJALyuban4+gPA+Mhwj/vLM'
    }
    proxy = "tp.a0ab.com:25517"
    proxies = {
        "https": "https://{0}".format(proxy),
        "http": "http://{0}".format(proxy),
    }
    params = {
        'merge': 0  # 0 合并, 1 返回注册局, 2 返回注册商
    }
    url = f'http://fdp.qianxin-inc.cn/v3/whois/reverse?column=email&value='+email+'&limit=100&orderbyDate=expiresDate&orderby=desc'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)
    result = []
    try:
        print(response.json()['data'])
        if need_active:
            for domain in response.json()['data']:
                url = f'http://fdp.qianxin-inc.cn/v3/whois/detail/' + domain + "?merge=0"
                rep = requests.request("GET", url, verify=False, headers=headers, proxies=proxies)
                try:
                    print(rep.json()["data"])

                    if rep.json()["data"]["registrantEmail"][0] == email and is_time_after_current(rep.json()["data"]["expiresDate"][0]):
                        result.append(domain)
                except Exception:
                    print(domain + " error", end="\t")
            return result
        else:
            return response.json()["data"]
    except Exception:
        traceback.print_exc()
        return None

def query_whois_by_name(name):
    headers = {
        'Connection': 'close',
        'fdp-access': 'c2ae6e5e6c914c54adad68caf6c55b2e',
        'fdp-secret': 'ekzPK2j+BiFp/ZOZ/Izz+pmsWAB/qdqPKNR2lUoAb6lDqndRtbocK6iDLqeK3XvTfYNASHlF5VUjDOunifYTYOIoc8XvCTCIak3XV0ZxprJALyuban4+gPA+Mhwj/vLM'
    }
    proxy = "tp.a0ab.com:25517"
    proxies = {
        "https": "https://{0}".format(proxy),
        "http": "http://{0}".format(proxy),
    }
    params = {
        'merge': 0  # 0 合并, 1 返回注册局, 2 返回注册商
    }
    url = f'http://fdp.qianxin-inc.cn/v3/whois/reverse?column=name&value='+name+'&limit=1000&orderbyDate=checkTime&orderby=desc'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)
    print(response.json()['data'])
    return response.json()['data']

def query_whois_by_phone(phone):
    headers = {
        'Connection': 'close',
        'fdp-access': 'c2ae6e5e6c914c54adad68caf6c55b2e',
        'fdp-secret': 'ekzPK2j+BiFp/ZOZ/Izz+pmsWAB/qdqPKNR2lUoAb6lDqndRtbocK6iDLqeK3XvTfYNASHlF5VUjDOunifYTYOIoc8XvCTCIak3XV0ZxprJALyuban4+gPA+Mhwj/vLM'
    }
    proxy = "tp.a0ab.com:25517"
    proxies = {
        "https": "https://{0}".format(proxy),
        "http": "http://{0}".format(proxy),
    }
    params = {
        'merge': 0  # 0 合并, 1 返回注册局, 2 返回注册商
    }
    url = f'http://fdp.qianxin-inc.cn/v3/whois/reverse?column=phone&value='+phone+'&limit=1000&orderbyDate=checkTime&orderby=desc'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)
    print(response.json()['data'])
    return response.json()['data']

def query_whois_by_org(org):
    headers = {
        'Connection': 'close',
        'fdp-access': 'c2ae6e5e6c914c54adad68caf6c55b2e',
        'fdp-secret': 'ekzPK2j+BiFp/ZOZ/Izz+pmsWAB/qdqPKNR2lUoAb6lDqndRtbocK6iDLqeK3XvTfYNASHlF5VUjDOunifYTYOIoc8XvCTCIak3XV0ZxprJALyuban4+gPA+Mhwj/vLM'
    }
    proxy = "tp.a0ab.com:25517"
    proxies = {
        "https": "https://{0}".format(proxy),
        "http": "http://{0}".format(proxy),
    }
    params = {
        'merge': 0  # 0 合并, 1 返回注册局, 2 返回注册商
    }
    url = f'http://fdp.qianxin-inc.cn/v3/whois/reverse?column=org&value='+org+'&limit=1000&orderbyDate=checkTime&orderby=desc'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)
    print(response.json()['data'])
    return response.json()['data']

def query_whois_by_nameserver(nameserver):
    headers = {
        'Connection': 'close',
        'fdp-access': 'c2ae6e5e6c914c54adad68caf6c55b2e',
        'fdp-secret': 'ekzPK2j+BiFp/ZOZ/Izz+pmsWAB/qdqPKNR2lUoAb6lDqndRtbocK6iDLqeK3XvTfYNASHlF5VUjDOunifYTYOIoc8XvCTCIak3XV0ZxprJALyuban4+gPA+Mhwj/vLM'
    }
    proxy = "tp.a0ab.com:25517"
    proxies = {
        "https": "https://{0}".format(proxy),
        "http": "http://{0}".format(proxy),
    }
    params = {
        'merge': 0  # 0 合并, 1 返回注册局, 2 返回注册商
    }
    url = f'http://fdp.qianxin-inc.cn/v3/whois/reverse?column=nameserver&value='+nameserver+'&limit=1000&orderbyDate=checkTime&orderby=desc'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)
    print(response.json()['data'])
    return response.json()['data']

def get_whois(domain):
    info = query_whois_detail(domain)
    d = {"email": "", "name": "", "phone": "", "org": ""}
    try:
        # print(info)
        if info["registrantEmail"] is not None and 'http' not in info["registrantEmail"][0] and 'privacy' not in info["registrantEmail"][0]:
            d["email"] = info["registrantEmail"][0]
    except Exception:
        # traceback.print_exc()
        print("", end="")
    try:
        if 'privacy' not in info["registrantName"][0]:
            d["name"] = info["registrantName"][0]
    except Exception:
        print("", end="")
    try:
        if 'privacy' not in info["registrantTelephone"][0]:
            d["phone"] = info["registrantTelephone"][0]
    except Exception:
        print("", end="")
    try:
        if 'privacy' not in info["registrantOrganization"][0]:
            d["org"] = info["registrantOrganization"][0]
    except Exception:
        print("", end="")
    return  d

#
# if __name__ == '__main__':
#     sys.setrecursionlimit(30000)
#
#     # 获取注册人信息部分
#     # 0420 domains
#     domains = ["neif.cn","szhzjz.com","czyxs.cn","baoshcn.com","miyou1688.com","beeed.cn","tuojie.top","huadiled.com.cn","helencn.com","huaqigj.cn","xingjitang.com.cn","huihanzi.com","ylwhy.org","szgasx.cn","rimou.top","haoyangsoft.com","danzhoumutangpingxin.cn","gzkedayiqi.com","mczj.com.cn","ssjr66.cn","hnweishi.com","lhjtea.com","cdbzx.top","frpjc.cn","kaibanle.cn","tuhaowang.cn","kyun.cn","shandongjinke.top","safebag.org.cn","dafuzhijia.com.cn","xkgcs.cn","sh-jiejin.com.cn","zhuandayup.cn","deyubao.com","tdzv.cn","lixiangsui.cn","arconobile.com","empress886.com.cn","qchen-qc.com","zajy.com.cn","fhyhy.com","260.com","cloud.com","reg30.cn","qypw.top","qiyu1018.top","mxyxpx.com","69.com","nq.cn","m7cewh.cn","sslst.top","hycapoj.cn","gxpqmgc.cn","xaxzhep.com","cxkh.net","casray.club","hfsibokeji.com","wangweibing.com","szstai.com","zhimei168.top","xinshiwuyou.cn","ls64.cn","tour-market.cn"]
#     # 0508
#     domains = ["cubbmks.cn",'v36hu2v.cn']
#     #0510
#     domains = ['zhimei168.top', 'exploric.cn', 'qypw.top', 'zhdwg.top', 'haoyangsoft.com', 'qiyu1018.top', 'zoompai.com', 'honganonline.cn', 'ssget.cn', 'tjwzly.com', 'casray.club', 'neif.cn', 'bjsongzhuang.com.cn', 'baoshcn.com', 'xsjxc.com', '836919126.com', 'ssjr66.cn', 'tuojie.top', 'yndhjzm.cn', 'ylt58.cn', 'tuhaowang.cn', 'afjrnol.cn', 'dianjiabao.com', 'xingjitang.com.cn', 'rifonda.cn', 'zgzsmhw.cn', 'xkgcs.cn', 'jinguyuan.com.cn', 'atauscn.cn', 'czyxs.cn', 'miyou1688.com', 'yaohong88.cn', 'hnweishi.com', 'pangaofeng.top', 'dqkingdee.com', 'jiulingyun.cn', 'jcjxjzg.cn', 'pzaqexm.cn', 'yjlzhj.cn', 'verov.top', 'www.ylt58.cn', 'com.cn', 'fhyhy.com', '69nq.cn', 'buildtolast.cn', 'castlewood.com.cn', 'mxyxpx.com', 'zoomkey.com.cn', 'fjchenfu.com', 'sytakad.cn', 'hfcgfc.com', 'gzluyuan.com', 'buysms.cn', 'miaomiaoxz.com', 'dengyubo.top', 'wangyaofeng.top', 'rkbcms.cn', 'anhuika.top', 'kechenyyp.cn', 'deyubao.com', 'yutenghb.com', 'bxgxcl.cn', 'unsuq.com', 'theskateboardschool.com', 'cloudee.com.cn', 'yiziyizi.cn', 'violintown.cn']
#     # spider domians
#     domains = ['zemakeji.com', 'dyshengtong.com', 'weldelite.cn', 'youhuangou.com', 'xlxq66.com', 'jspyhb.com', 'sdkuma.com', 'jisujsq.com', 'xmnk.cn', 'na-do.com', 'lizhelawyer.com', 'dlunitedmining.com', 'huezk.com', 'jsnjdz.com', 'haodewj.cn', 'long120.net', 'ceo120.net', 'hospitalkowloon.com', 'jzltzfw.com', 'zsyycrz.com', 'huahaiweb.com', 'woqichuxing.cn', 'shqianlx.com', 'nblvdong.com', 'baoshcn.com', 'hkyzz.net', 'qq.com', 'fhyhy.com', 'scslk.com', 'ximengnaikang.com', 'shssj.net', 'zhjunjia.cn', 'tencentcs.com', 'yizhaobiao.net', 'monluxe.cn', 'kiavid.com', 'qdtmjgjt.com', 'kaopu001.com', 'chstar.com.cn', 'intspire.net', 'cthysq.cn', 'shjiulong.cn']
#     # all截止0517
#     domains = ["zhuandayup.cn","xaxzhep.com","dzzpgs.cn","deyubao.com","whslsz.cn","zainan.com.cn","yumijy.cn","woqichuxing.cn","leu17.com","aaak.top","cxkh.net","ylwhy.org","ynjinlong.cn","zhimei168.top","gzkedayiqi.com","bfdbt.net.cn","260cloud.com","8n3nqq1.buzz","dlunitedmining.com","dafuzhijia.com.cn","hanshangz.com","pangaofeng.top","ssjr66.cn","atauscn.cn","szwekq.com","mczj.com.cn","xn--1rwm9b515f.cn","xn--pbt333iujj.cn","haechi.top","huadiled.com.cn","shssj.net","zgbaohong.com","wangqing15.top","hxinyun.cn","jindouzi123.com","szgasx.cn","reg30.cn","yunhehd.com","69nq.cn","blasoul.com","hjgkfl.cn","shandonghuiyang.com","caowensong.top","jsnjdz.com","5mkskww.buzz","enjoyvision.cn","louisonwoodworks.com","wztqq.cn","hospitalkowloon.com","xmnk.cn","0t7lpgklny.xyz","lixiangsui.cn","ai6lc6zblm.xyz","uz39.com","fwba3x.cn","danzhoumutangpingxin.cn","mbpckbp.cn","kyun.cn","82028.com.cn","hnmjwlkj.cn","verov.top","cubbmks.cn","mmwhh.top","dczkw.cn","jsl6.top","chengjgy.cn","qgltv.top","tour-market.cn","shandongjinke.top","violintown.cn","shanxiangyhq.top","hnjcps.com","yunbokongjian.top","bailianwei.top","wxhsc.cn","jzltzfw.com","xinshiwuyou.cn","ylt58.cn","zcbgfsh.cn","evogcckc1s.xyz","zzwjbjfw.cn","shanleishiye.com","sdcyyc.com","xiaobiesan.top","7yzah.cn","xingjitang.com.cn","bxgxcl.cn","wushengkai.top","jpjboke.top","xn--ekrq5w1jh.cn","xinyunde.cn","xuejiejiaoyu.cn","sslst.top","fsyun.top","upvcu.com","jcjxjzg.cn","qchen-qc.com","nt23n.cn","hhs0906.top","hzfangji.com","zhjunjia.cn","feixianw.com","xylol.top","szhzjz.com","yvi6pd.cn","casray.club","zugehao.cc","qlcwxrx.cn","unsuq.com","aceedu.net.cn","kmbviak.cn","vepx.cn","ufaljip.cn","lzminbai.com.cn","action2017.top","youranplus.cn","xn--p5tw4lnuf.cn","sqlt.cn","baoshcn.com","daishuzhuanqian.cn","shidu168.com","mazhuangxinge.top","jinguyuan.com.cn","yizhaobiao.net","qp84.top","yangkaihong.cn","wztcb.cn","gl3vopc4kv.xyz","foremostgroup.com","mbme.cn","lzlongjiang.cn","ymlmtaz.cn","youlianjiaoyi.cn","rhdur61.top","aad9.cn","zgzszq.com","xn--qrq020a6tn9oi.cn","cdbzx.top","ismile.org.cn","locnbtz.cn","m7cewh.cn","yaohong88.cn","ls64.cn","nhmspkmhg4.xyz","zgzsmhw.cn","rimou.top","jszkfy.cn","kaibanle.cn","njjdkt.com","hfsibokeji.com","shangzhongxia.cn","theskateboardschool.com","xn--qiv838a.cc","daybuday1.top","lhjtea.com","ywj1314.top","xkgcs.cn","you100.top","nachanghefengjiazheng.cn","ychat01.win","dogbk.com","yingangxinxizixun.cn","safebag.org.cn","ketwy4s5sr.xyz","jkhxdc.com","szsyhs.cn","vis-nicety.cn","anhuika.top","yqhsdcar.cn","arconobile.com","wuhantu.top","haoyangsoft.com","miyou1688.com","buysms.cn","shqianlx.com","hair-welfare.top","baoqih2.cn","jhsw2014.cn","zsmkswkj.com","dltwo.top","hwj123.net","ewwlzuz.cn","gdzshr.com","greenforesight.cn","wmzhe.com","9dfgn.cn","jsswj.org.cn","firepointsoft.com.cn","szcwjs.com","hfcgfc.com","vv0l4cojdp.xyz","czyxs.cn","wofodao.com","hkiwc.top","zhenggang.net.cn","gzluyuan.com","zhdwg.top","voii.top","afjrnol.cn","ak561.cn","tuojie.top","dijmjke.cn","tengneng.cn","jiaoyimao21.buzz","6ss.top","huyundun.com","szlbjc.com","baisongshangjie.cn","incyxwu.cn","goivrdp.cn","beeed.cn","chenyunxin.cn","nbhsjdz.com","ahyyzn.com","cardiffkabel.com.cn","tuxugn.com","jxlfqc.com","aivxxt.com","ledartek.cn","neif.cn","tdzv.cn","ziemnmj.cn","xiulie.top","yuandaotax.com","ly-jddz.cn","huazhiqinfs.cn","xn--44qr78f93b.cn","77mz.cn","fatech.online","87x6eod.buzz","kechenyyp.cn","changhesteel.cn","qq9kiwsl9o.xyz","phmxa5j8jf.xyz","wvpxyhc.cn","hycapoj.cn","wdbjz.cn","huihanzi.com","sbzyccj.com","szstai.com","sdpjmedia.cn","fkxjk.top","tjwzly.com","sqwjj.top","wykl.top","frpjc.cn","xiaonuomi.com.cn","hcyuee.top","aifenxiang88.top","blwdkhj.cn","fjchenfu.com","hhllmc.top","xn--iiqpw446m.cn","xyfzmy.com","kingdeepy.com","zhihuiyunying.cn","helencn.com","becstar.cn","rto4mimdby.xyz","hlehuo.com","qfjfcty1.cn","sixclouds.cn","imaofg.top","hfxfrfdt.cn","xlwsdp.cn","hlvdhse.cn","fhyhy.com","ymcvolt.cn","tppuvhh0ix.xyz","gxpqmgc.cn","gpufix.top","a3v7m2m.top","buz23qb5.cn","rifonda.cn","mjjx168.com","zcgyjx.com","huaqigj.cn","jswuye.com.cn","castlewood.com.cn","chinacowb.com","yxshhb.com.cn","4006wosign.com","mxyxpx.com","bjsongzhuang.com.cn","huanhaoinc.com","cicycat.com","sh-jiejin.com.cn","ovemlqt.cn","huahaiweb.com","sdsqzn.com","intspire.net","tuhaowang.cn","sky58.cn","zzjdi.top","amberfans.com.cn","yytgj.top","zajy.com.cn","krbova-kamna-krby.com","grand-millennium.cn","hee0pfl8w4.xyz","9pmskzn.buzz","cbgbxyxzx.cn","acregulator.com.cn","baidu.com","hdqb267.cn","kukaestrategia.com","ppneea.cn","qiyu1018.top","riurl.cn","haokao123.com","btstbj.com","91gwy.net","dnovos.com","maxiaoliang.top","oexlsua.cn","youxigujia.com","sinocrownsd.cn","xhw1.cn","letnt7idr9.xyz","sdkuma.com","qypw.top","sytakad.cn","wangweibing.com","esastur.com","empress886.com.cn","mashajihaha.top","youxucoding.top","firstaidb.top","836919126.com","web1236.top","hnweishi.com","honganonline.cn","aemashf.cn","zmserver.top","shangnanseo.top","xianhou88.com","qoa.cn","yjyt.net.cn","sl-zhks.top"]
#     print(len(domains))
#     d = {}
#     emails = set()
#     names = set()
#     orgs = set()
#     phones = set()
#     status = set()
#     for domain in domains:
#         try:
#             print("",end="")
#             # domain = domain.split("/")[2]
#             # domain = domain.replace()
#             # print(domain,end=":")
#         except Exception:
#             print("ee")
#         info = query_whois_detail(domain)
#         print(info)
#
#         d[domain] = {"email": "", "name":"", "phone": "", "org": "","status": ""}
#         try:
#             if 'http' not in info["registrantEmail"][0] and 'privacy' not in info["registrantEmail"][0]:
#                 emails.add(info["registrantEmail"][0])
#                 d[domain]["email"] = info["registrantEmail"][0]
#         except Exception:
#             print("",end="")
#         try:
#             if 'privacy' not in info["registrantName"][0]:
#                 names.add(info["registrantName"][0])
#                 d[domain]["name"] = info["registrantName"][0]
#         except Exception:
#             print("",end="")
#         try:
#             if 'privacy' not in info["registrantTelephone"][0]:
#                 phones.add(info["registrantTelephone"][0])
#                 d[domain]["phone"] = info["registrantTelephone"][0]
#         except Exception:
#             print("",end="")
#         try:
#             if 'privacy' not in info["registrantOrganization"][0]:
#                 orgs.add(info["registrantOrganization"][0])
#                 d[domain]["org"] = info["registrantOrganization"][0]
#         except Exception:
#             print("",end="")
#         try:
#             d[domain]["status"] = history['status'][0]
#
#     with open("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/reverse_method/draft.json",'a') as f:
#         f.write(str(d))
#     print(emails)
#     print(names)
#     print(phones)
#     print(orgs)
