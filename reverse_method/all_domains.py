
import os
import sys

# import magic
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
sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/config/")

from config.db import DB
from config.log import Log
# tag = "email"
# table = "domains_from_" + tag
db = DB()
logger = Log()
# mongo1 = db.get_mongo()['fraud_detection'][table]
# datas = mongo1.find()
# ds = set()
# for x in datas:
#     ds = ds.union(set(x["domains_list"]))
# print(ds)

table = 'fake_game_domain_info'
mongo2 = db.get_mongo()['fraud_detection'][table]
d = [x for x in mongo2.find()]
domains = ["zhuandayup.cn","xaxzhep.com","dzzpgs.cn","deyubao.com","whslsz.cn","zainan.com.cn","yumijy.cn","woqichuxing.cn","leu17.com","aaak.top","cxkh.net","ylwhy.org","ynjinlong.cn","zhimei168.top","gzkedayiqi.com","bfdbt.net.cn","260cloud.com","8n3nqq1.buzz","dlunitedmining.com","dafuzhijia.com.cn","hanshangz.com","pangaofeng.top","ssjr66.cn","atauscn.cn","szwekq.com","mczj.com.cn","xn--1rwm9b515f.cn","xn--pbt333iujj.cn","haechi.top","huadiled.com.cn","shssj.net","zgbaohong.com","wangqing15.top","hxinyun.cn","jindouzi123.com","szgasx.cn","reg30.cn","yunhehd.com","69nq.cn","blasoul.com","hjgkfl.cn","shandonghuiyang.com","caowensong.top","jsnjdz.com","5mkskww.buzz","enjoyvision.cn","louisonwoodworks.com","wztqq.cn","hospitalkowloon.com","xmnk.cn","0t7lpgklny.xyz","lixiangsui.cn","ai6lc6zblm.xyz","uz39.com","fwba3x.cn","danzhoumutangpingxin.cn","mbpckbp.cn","kyun.cn","82028.com.cn","hnmjwlkj.cn","verov.top","cubbmks.cn","mmwhh.top","dczkw.cn","jsl6.top","chengjgy.cn","qgltv.top","tour-market.cn","shandongjinke.top","violintown.cn","shanxiangyhq.top","hnjcps.com","yunbokongjian.top","bailianwei.top","wxhsc.cn","jzltzfw.com","xinshiwuyou.cn","ylt58.cn","zcbgfsh.cn","evogcckc1s.xyz","zzwjbjfw.cn","shanleishiye.com","sdcyyc.com","xiaobiesan.top","7yzah.cn","xingjitang.com.cn","bxgxcl.cn","wushengkai.top","jpjboke.top","xn--ekrq5w1jh.cn","xinyunde.cn","xuejiejiaoyu.cn","sslst.top","fsyun.top","upvcu.com","jcjxjzg.cn","qchen-qc.com","nt23n.cn","hhs0906.top","hzfangji.com","zhjunjia.cn","feixianw.com","xylol.top","szhzjz.com","yvi6pd.cn","casray.club","zugehao.cc","qlcwxrx.cn","unsuq.com","aceedu.net.cn","kmbviak.cn","vepx.cn","ufaljip.cn","lzminbai.com.cn","action2017.top","youranplus.cn","xn--p5tw4lnuf.cn","sqlt.cn","baoshcn.com","daishuzhuanqian.cn","shidu168.com","mazhuangxinge.top","jinguyuan.com.cn","yizhaobiao.net","qp84.top","yangkaihong.cn","wztcb.cn","gl3vopc4kv.xyz","foremostgroup.com","mbme.cn","lzlongjiang.cn","ymlmtaz.cn","youlianjiaoyi.cn","rhdur61.top","aad9.cn","zgzszq.com","xn--qrq020a6tn9oi.cn","cdbzx.top","ismile.org.cn","locnbtz.cn","m7cewh.cn","yaohong88.cn","ls64.cn","nhmspkmhg4.xyz","zgzsmhw.cn","rimou.top","jszkfy.cn","kaibanle.cn","njjdkt.com","hfsibokeji.com","shangzhongxia.cn","theskateboardschool.com","xn--qiv838a.cc","daybuday1.top","lhjtea.com","ywj1314.top","xkgcs.cn","you100.top","nachanghefengjiazheng.cn","ychat01.win","dogbk.com","yingangxinxizixun.cn","safebag.org.cn","ketwy4s5sr.xyz","jkhxdc.com","szsyhs.cn","vis-nicety.cn","anhuika.top","yqhsdcar.cn","arconobile.com","wuhantu.top","haoyangsoft.com","miyou1688.com","buysms.cn","shqianlx.com","hair-welfare.top","baoqih2.cn","jhsw2014.cn","zsmkswkj.com","dltwo.top","hwj123.net","ewwlzuz.cn","gdzshr.com","greenforesight.cn","wmzhe.com","9dfgn.cn","jsswj.org.cn","firepointsoft.com.cn","szcwjs.com","hfcgfc.com","vv0l4cojdp.xyz","czyxs.cn","wofodao.com","hkiwc.top","zhenggang.net.cn","gzluyuan.com","zhdwg.top","voii.top","afjrnol.cn","ak561.cn","tuojie.top","dijmjke.cn","tengneng.cn","jiaoyimao21.buzz","6ss.top","huyundun.com","szlbjc.com","baisongshangjie.cn","incyxwu.cn","goivrdp.cn","beeed.cn","chenyunxin.cn","nbhsjdz.com","ahyyzn.com","cardiffkabel.com.cn","tuxugn.com","jxlfqc.com","aivxxt.com","ledartek.cn","neif.cn","tdzv.cn","ziemnmj.cn","xiulie.top","yuandaotax.com","ly-jddz.cn","huazhiqinfs.cn","xn--44qr78f93b.cn","77mz.cn","fatech.online","87x6eod.buzz","kechenyyp.cn","changhesteel.cn","qq9kiwsl9o.xyz","phmxa5j8jf.xyz","wvpxyhc.cn","hycapoj.cn","wdbjz.cn","huihanzi.com","sbzyccj.com","szstai.com","sdpjmedia.cn","fkxjk.top","tjwzly.com","sqwjj.top","wykl.top","frpjc.cn","xiaonuomi.com.cn","hcyuee.top","aifenxiang88.top","blwdkhj.cn","fjchenfu.com","hhllmc.top","xn--iiqpw446m.cn","xyfzmy.com","kingdeepy.com","zhihuiyunying.cn","helencn.com","becstar.cn","rto4mimdby.xyz","hlehuo.com","qfjfcty1.cn","sixclouds.cn","imaofg.top","hfxfrfdt.cn","xlwsdp.cn","hlvdhse.cn","fhyhy.com","ymcvolt.cn","tppuvhh0ix.xyz","gxpqmgc.cn","gpufix.top","a3v7m2m.top","buz23qb5.cn","rifonda.cn","mjjx168.com","zcgyjx.com","huaqigj.cn","jswuye.com.cn","castlewood.com.cn","chinacowb.com","yxshhb.com.cn","4006wosign.com","mxyxpx.com","bjsongzhuang.com.cn","huanhaoinc.com","cicycat.com","sh-jiejin.com.cn","ovemlqt.cn","huahaiweb.com","sdsqzn.com","intspire.net","tuhaowang.cn","sky58.cn","zzjdi.top","amberfans.com.cn","yytgj.top","zajy.com.cn","krbova-kamna-krby.com","grand-millennium.cn","hee0pfl8w4.xyz","9pmskzn.buzz","cbgbxyxzx.cn","acregulator.com.cn","hdqb267.cn","kukaestrategia.com","ppneea.cn","qiyu1018.top","riurl.cn","haokao123.com","btstbj.com","91gwy.net","dnovos.com","maxiaoliang.top","oexlsua.cn","youxigujia.com","sinocrownsd.cn","xhw1.cn","letnt7idr9.xyz","sdkuma.com","qypw.top","sytakad.cn","wangweibing.com","esastur.com","empress886.com.cn","mashajihaha.top","youxucoding.top","firstaidb.top","836919126.com","web1236.top","hnweishi.com","honganonline.cn","aemashf.cn","zmserver.top","shangnanseo.top","xianhou88.com","qoa.cn","yjyt.net.cn","sl-zhks.top"]
for domain in domains:
    has = False
    for da in d:
        if domain == da["domain"]:
            has = True
            print(domain+"|"+da['ip']+"|"+str(da['status']["0"]))
            break
    if not has:
        print(domain+" None")