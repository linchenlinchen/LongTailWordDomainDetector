import traceback

import requests


def query_sld_traffic(domain, start_time='20230501', end_time='20230614', domain_type='sld',
                      proxies={'http': 'tp.a0ab.com:25517', 'https': 'tp.a0ab.com:25517'}):
    params = {
        'start': start_time,
        'end': end_time,
        'type': domain_type
    }
    headers = {
        'Connection': 'close',
        'fdp-access': 'a57870a7bb9b47c48bff945c70fc8e95',
        'fdp-secret': 'syyAiQ8cnqz5FfrpUFKK/1VQQYU4ZBITl7Ic2ppuSN7vsNgKP5f8D5bZpUPMYSJBlJJzWRkY5CmTkVGvSWxEWqs3yTWjhLW4RO6rpp0b4L8='
    }
    url = f'http://fdp.qianxin-inc.cn/v3/trends/{domain}'
    response = requests.request("GET", url, params=params, verify=False, headers=headers, proxies=proxies)
    try:
        print(response.json()["data"])
    except:
        traceback.print_exc()
        return []
    return [x for x in response.json()['data']]


def generate_date_arr(m1, d1, m2, d2):
    from datetime import datetime, timedelta

    start_date = datetime(2023, m1, d1)
    end_date = datetime(2023, m2, d2)
    date_array = []
    current_date = start_date
    while current_date <= end_date:
        date_array.append(current_date.strftime("%Y%m%d"))
        current_date += timedelta(days=1)
    return date_array


# domains = ["zhuandayup.cn", "xaxzhep.com", "dzzpgs.cn", "deyubao.com", "whslsz.cn", "zainan.com.cn", "yumijy.cn",
#            "woqichuxing.cn", "leu17.com", "aaak.top", "cxkh.net", "ylwhy.org", "ynjinlong.cn", "zhimei168.top",
#            "gzkedayiqi.com", "bfdbt.net.cn", "260cloud.com", "8n3nqq1.buzz", "dlunitedmining.com", "dafuzhijia.com.cn",
#            "hanshangz.com", "pangaofeng.top", "ssjr66.cn", "atauscn.cn", "szwekq.com", "mczj.com.cn",
#            "xn--1rwm9b515f.cn", "xn--pbt333iujj.cn", "haechi.top", "huadiled.com.cn", "shssj.net", "zgbaohong.com",
#            "wangqing15.top", "hxinyun.cn", "jindouzi123.com", "szgasx.cn", "reg30.cn", "yunhehd.com", "69nq.cn",
#            "blasoul.com", "hjgkfl.cn", "shandonghuiyang.com", "caowensong.top", "jsnjdz.com", "5mkskww.buzz",
#            "enjoyvision.cn", "louisonwoodworks.com", "wztqq.cn", "hospitalkowloon.com", "xmnk.cn", "0t7lpgklny.xyz",
#            "lixiangsui.cn", "ai6lc6zblm.xyz", "uz39.com", "fwba3x.cn", "danzhoumutangpingxin.cn", "mbpckbp.cn",
#            "kyun.cn", "82028.com.cn", "hnmjwlkj.cn", "verov.top", "cubbmks.cn", "mmwhh.top", "dczkw.cn", "jsl6.top",
#            "chengjgy.cn", "qgltv.top", "tour-market.cn", "shandongjinke.top", "violintown.cn", "shanxiangyhq.top",
#            "hnjcps.com", "yunbokongjian.top", "bailianwei.top", "wxhsc.cn", "jzltzfw.com", "xinshiwuyou.cn", "ylt58.cn",
#            "zcbgfsh.cn", "evogcckc1s.xyz", "zzwjbjfw.cn", "shanleishiye.com", "sdcyyc.com", "xiaobiesan.top",
#            "7yzah.cn", "xingjitang.com.cn", "bxgxcl.cn", "wushengkai.top", "jpjboke.top", "xn--ekrq5w1jh.cn",
#            "xinyunde.cn", "xuejiejiaoyu.cn", "sslst.top", "fsyun.top", "upvcu.com", "jcjxjzg.cn", "qchen-qc.com",
#            "nt23n.cn", "hhs0906.top", "hzfangji.com", "zhjunjia.cn", "feixianw.com", "xylol.top", "szhzjz.com",
#            "yvi6pd.cn", "casray.club", "zugehao.cc", "qlcwxrx.cn", "unsuq.com", "aceedu.net.cn", "kmbviak.cn",
#            "vepx.cn", "ufaljip.cn", "lzminbai.com.cn", "action2017.top", "youranplus.cn", "xn--p5tw4lnuf.cn", "sqlt.cn",
#            "baoshcn.com", "daishuzhuanqian.cn", "shidu168.com", "mazhuangxinge.top", "jinguyuan.com.cn",
#            "yizhaobiao.net", "qp84.top", "yangkaihong.cn", "wztcb.cn", "gl3vopc4kv.xyz", "foremostgroup.com", "mbme.cn",
#            "lzlongjiang.cn", "ymlmtaz.cn", "youlianjiaoyi.cn", "rhdur61.top", "aad9.cn", "zgzszq.com",
#            "xn--qrq020a6tn9oi.cn", "cdbzx.top", "ismile.org.cn", "locnbtz.cn", "m7cewh.cn", "yaohong88.cn", "ls64.cn",
#            "nhmspkmhg4.xyz", "zgzsmhw.cn", "rimou.top", "jszkfy.cn", "kaibanle.cn", "njjdkt.com", "hfsibokeji.com",
#            "shangzhongxia.cn", "theskateboardschool.com", "xn--qiv838a.cc", "daybuday1.top", "lhjtea.com",
#            "ywj1314.top", "xkgcs.cn", "you100.top", "nachanghefengjiazheng.cn", "ychat01.win", "dogbk.com",
#            "yingangxinxizixun.cn", "safebag.org.cn", "ketwy4s5sr.xyz", "jkhxdc.com", "szsyhs.cn", "vis-nicety.cn",
#            "anhuika.top", "yqhsdcar.cn", "arconobile.com", "wuhantu.top", "haoyangsoft.com", "miyou1688.com",
#            "buysms.cn", "shqianlx.com", "hair-welfare.top", "baoqih2.cn", "jhsw2014.cn", "zsmkswkj.com", "dltwo.top",
#            "hwj123.net", "ewwlzuz.cn", "gdzshr.com", "greenforesight.cn", "wmzhe.com", "9dfgn.cn", "jsswj.org.cn",
#            "firepointsoft.com.cn", "szcwjs.com", "hfcgfc.com", "vv0l4cojdp.xyz", "czyxs.cn", "wofodao.com", "hkiwc.top",
#            "zhenggang.net.cn", "gzluyuan.com", "zhdwg.top", "voii.top", "afjrnol.cn", "ak561.cn", "tuojie.top",
#            "dijmjke.cn", "tengneng.cn", "jiaoyimao21.buzz", "6ss.top", "huyundun.com", "szlbjc.com",
#            "baisongshangjie.cn", "incyxwu.cn", "goivrdp.cn", "beeed.cn", "chenyunxin.cn", "nbhsjdz.com", "ahyyzn.com",
#            "cardiffkabel.com.cn", "tuxugn.com", "jxlfqc.com", "aivxxt.com", "ledartek.cn", "neif.cn", "tdzv.cn",
#            "ziemnmj.cn", "xiulie.top", "yuandaotax.com", "ly-jddz.cn", "huazhiqinfs.cn", "xn--44qr78f93b.cn", "77mz.cn",
#            "fatech.online", "87x6eod.buzz", "kechenyyp.cn", "changhesteel.cn", "qq9kiwsl9o.xyz", "phmxa5j8jf.xyz",
#            "wvpxyhc.cn", "hycapoj.cn", "wdbjz.cn", "huihanzi.com", "sbzyccj.com", "szstai.com", "sdpjmedia.cn",
#            "fkxjk.top", "tjwzly.com", "sqwjj.top", "wykl.top", "frpjc.cn", "xiaonuomi.com.cn", "hcyuee.top",
#            "aifenxiang88.top", "blwdkhj.cn", "fjchenfu.com", "hhllmc.top", "xn--iiqpw446m.cn", "xyfzmy.com",
#            "kingdeepy.com", "zhihuiyunying.cn", "helencn.com", "becstar.cn", "rto4mimdby.xyz", "hlehuo.com",
#            "qfjfcty1.cn", "sixclouds.cn", "imaofg.top", "hfxfrfdt.cn", "xlwsdp.cn", "hlvdhse.cn", "fhyhy.com",
#            "ymcvolt.cn", "tppuvhh0ix.xyz", "gxpqmgc.cn", "gpufix.top", "a3v7m2m.top", "buz23qb5.cn", "rifonda.cn",
#            "mjjx168.com", "zcgyjx.com", "huaqigj.cn", "jswuye.com.cn", "castlewood.com.cn", "chinacowb.com",
#            "yxshhb.com.cn", "4006wosign.com", "mxyxpx.com", "bjsongzhuang.com.cn", "huanhaoinc.com", "cicycat.com",
#            "sh-jiejin.com.cn", "ovemlqt.cn", "huahaiweb.com", "sdsqzn.com", "intspire.net", "tuhaowang.cn", "sky58.cn",
#            "zzjdi.top", "amberfans.com.cn", "yytgj.top", "zajy.com.cn", "krbova-kamna-krby.com", "grand-millennium.cn",
#            "hee0pfl8w4.xyz", "9pmskzn.buzz", "cbgbxyxzx.cn", "acregulator.com.cn", "hdqb267.cn", "kukaestrategia.com",
#            "ppneea.cn", "qiyu1018.top", "riurl.cn", "haokao123.com", "btstbj.com", "91gwy.net", "dnovos.com",
#            "maxiaoliang.top", "oexlsua.cn", "youxigujia.com", "sinocrownsd.cn", "xhw1.cn", "letnt7idr9.xyz",
#            "sdkuma.com", "qypw.top", "sytakad.cn", "wangweibing.com", "esastur.com", "empress886.com.cn",
#            "mashajihaha.top", "youxucoding.top", "firstaidb.top", "836919126.com", "web1236.top", "hnweishi.com",
#            "honganonline.cn", "aemashf.cn", "zmserver.top", "shangnanseo.top", "xianhou88.com", "qoa.cn", "yjyt.net.cn",
#            "sl-zhks.top", "gxebfxi.cn", "xn--w2x90pk6p.cn", "88sup.com", "nvodldk.cn", "fristblood.top", "haitaopai.cn",
#            "hzthealth.com", "yypyq.cn", "xxweb.top", "wwzlxf.top", "vgbhynv.com", "haogugu.vip",
#            "albuquerquecareerfairs.com", "shandongdingyi.cn", "qfy8.com", "szyc56.com", "hhinternational.com.cn",
#            "qzbarwx.cn", "88ymxd.top", "jjdhvpz.cn", "jdvsbnt.cn", "tw920.com", "henchang.cn", "jtjklm.top",
#            "hurstjeepster.com", "dlrm.com.cn", "xilai2017.cn", "m01.com.cn", "tuokeb2b.net", "dplejd.com", "pssb.top",
#            "xtjlks.cn", "wztca.cn", "sxonekey.cn", "jink168.top", "xn--h6q36cd4we1j.cn", "cdjjcz.cn", "sangge.top",
#            "aliyun6969.cn", "caoxiantv.com", "weifangfojiao.com", "ximengnaikang.com", "hpmen.com",
#            "choiceautorepairs.com", "baidugww.com", "fwift.com", "disimju.cn", "mdoys.cn", "y8qf.com", "jhkj10.top",
#            "fuxgj.cn", "ailvgoserver.com", "ep37.com", "haisheng-dl.com", "zwldmj.top", "qdakdp.cn", "gyhb666.com",
#            "htuidc.com", "youhuangou.com", "vensigpt.com", "tcfabu.cn", "buildtolast.cn", "yondoor.com", "xmd88.cn",
#            "luyitongxun.cn", "zhaishiwang.com.cn", "zjz616.com", "51sohu.com", "8645.com.cn", "pc9.com",
#            "shangquan2021.cn", "hljykxsm.cn", "fkyun.com", "pywb.net", "y7o.cn", "shachuangxingcai.com", "52rou.cn",
#            "nrfysmm.cn", "yuanlinshej.com", "teurl.cn", "cnugveq.cn", "wttewrc.cn", "aliaviation.com", "yutenghb.com",
#            "ifcxx.com", "xingdongi.com", "eonly.cn", "runbible.cn", "z12.cn", "zycsdhr.top", "t2t.org.cn",
#            "liverpoolnewstoday.com", "dqgqb.net", "gthjsc.cn", "nltfvop.cn", "bonuojiaju.cn", "meituangeek.com",
#            "kepandown.top", "zjhssc.cn", "qtizygf.com.cn", "bangwx.cn", "szmmd.cn", "liaokong.com", "senkekeji.cn",
#            "aimek.cn", "bievotech.cn", "grapewall.cn", "gzqbc.cn", "hnjingzun.cn", "esscs.cn", "fjlngan.cn",
#            "vamqses.cn", "frbg.cn", "guanshifuwu.com", "zemakeji.com", "cqqzj.net.cn", "uwwhunx.cn", "llzhuan.top",
#            "qvq75z3.cn", "hzzunhuang.com", "cknhcgzxmv.cn", "dmhevuv.cn", "ksy.com", "wookeer.com", "lzxf.com.cn",
#            "gurumenomori.com", "bxnszs.cn", "51kuaixue.cn", "shenpinpin.com", "paidui1.cn", "bmhq.cn", "jleh.cn",
#            "10host.cn", "playwater.com.cn", "tytxsj.cn", "bhsljt.cn", "cciccc.com", "xlxq66.com", "ideiadinheiro.com",
#            "blenderkit.cn", "hxwszf.cn", "sufavalve.cn", "zion-cn.com", "inxin.com.cn", "gwmeeju.cn", "mhshwxb.cn",
#            "helpinfo.net", "uosbox.cn", "shishanzhen.com", "cgsteels.cn", "msmzb.com", "utopiaecologica.com",
#            "interhash.top", "fy-zm.cn", "yjlzhj.cn", "cscsw.cn", "hljyww.cn", "ycyxf.cn", "123jinchan.cn", "valovfw.cn",
#            "ephnsgj.cn", "gmocso.cn", "aotjo.com", "dongfengru1.cn", "stcmoet.cn", "sxjtzl.com", "nyin.top",
#            "hfgxkj.cn", "wztql.cn", "wglab.cn", "tantuwo.com", "kanglietie.com", "xxdntjx.com", "gkymljs.cn",
#            "uvepvlx.cn", "123jl.cn", "sbw1688.com", "shenfux.top", "sdhxrs.cn", "54ca.top", "quzhouy.com",
#            "qingshang888888.com.cn", "ljzwj.com", "liujunsh.cn", "yeyou.com", "zghuixin.com.cn", "covilla.com",
#            "ceo120.net", "cstly.cn", "sapflvx.cn", "quanjingkj.com", "pingda56.cn", "90hbw.com", "mhhtzl.com",
#            "2chuyou.cn", "gjp9.cn", "bc-4.com", "wlgnjd.com", "sdyudi.cn", "chstar.com.cn", "xsjxc.com",
#            "baihuowang.com.cn", "avpt.cn", "sungdo.cc", "weldelite.cn", "kdpost.top", "1rbrb9.cn",
#            "fengzhiconsulting.com.cn", "jspyhb.com", "577ka.cn", "xttjnk.com", "jinkangzheng.com", "bztchlkj.cn",
#            "xn--rhty0to3g5o0byep.cn", "okacomco.com", "v36hu2v.cn", "scslk.com", "qsigdyr.cn", "ghcj.com.cn",
#            "brelly.com.cn", "ppyt.cn", "thevoidacademy.com", "ncxyb.com", "xmanna.cn", "lfx668.com", "chenjiagou.top",
#            "oiuknll.cn", "skx19980524.top", "jnoyzia.cn", "moropower.com", "caoqian.top", "lshcc.com", "yxgvojq.cn",
#            "qhtongda.cn", "92055.cn", "qingjianb.cn", "ttxgy.top", "srnet.com.cn", "glkaiyuan.com.cn", "tmvppwl.cn",
#            "edison666.top", "fneptft.cn", "lcnclqy.cn", "bbdwr.com", "hoyu1832.com", "dengyubo.top", "pay722.com",
#            "fisnake.cc", "007v.cn", "monluxe.cn", "cutbqse.cn", "lernachowinner.com", "kmbtva.cn", "cuixiaodong.cn",
#            "edsajfl.cn", "longyidao.top", "haiganghld.com", "paintcreekproperty.com", "aixinyudz.com",
#            "cdtceram.com.cn", "jobonhouse.com", "xn--xhqr21n.net", "wanhezhiyao.cn", "gmail2.cn", "wkkczxy.cn",
#            "zzsaisite.cn", "itranz.cn", "diyiyuesao.cn"]
# domains = ["aynzzj.com","californiasunshinebaby.com","fanhaishuzhi.com","hrbxd.top","kangzhongyigong.cn","meijabao.cn","otryinfo.com","wangadou.top","ym56.cn","zgmsdwt.cn","ben-architects.com","dxjskj.com","fjhnyb.cn","ibaritz.com","kindun.cn","mgjbshengri.cn","pxsy.org.cn","xuanyao.sh.cn","yssyyey.cn","zjgjbjx.com","bult99.com","dylansillage.cn","flyfz.top","juanletao.top","lifestlye-us.com","ncwlkq.cn","rxxlsc.cn","ykh6.com","yxzqtfa.com","zzeaststar.com"]
# domains = ["271692.com","cdfcqy.cn","gdysry.cn","jingrenhe.com","papier-peint-jungle.com.shzmyq.com","tydld.com","xazxrl.com","888door.cn","chendamuye.com","gemgpt.org","jjkp.cn","petsnohomeless.com","sicstech.cn","vatlytrilieutainhathientam.com","yanzhaoban.cn","98wcy.cn","cracklogs.com","golazadabuyx.com","jx2580.com","phpanalytic.com","sunglassess.top","vip-car.com.cn","yoqu.fun","ahdyjb.xyz","csworldlet.top","gztzcxs.com","kingstar-light.com","qinuo2013.cn","tedc.org.cn","virider.com","yuea981008.cn","am-music.fr","dgytjh.com","haydentradingcompany.com","leannie.cn","sanbaishou.com","thanhfarm.com","voldado.com","yykw.cn","anhuiskj.com","escobar2.com","hbbjcy.com","lemirellc.com","sdsssw.cn","tlyzyhxt.cn","volidshop.ru","zikao001.cn","bedahminat.com","fengooo.com","hcdesdeccd.cn","lijifeng.cn","shopmultimart.com","tmww.cn","wealthmosesministries.org","zjswjx.cn","bj-wxxc.com","ffzxwz13.cn","igoodlife.cn","lycxhbsb.com","shunyicardiology.cn","traztech.ca","weciimaa.online","zxuekai.com","bjyjch.cn","fhjh.cn","j120-2.cn","oedda.com","shzhqbhshls.com","trippindaizy.store","xayh56.cn"]
domains = []
with open("../test/tmp", 'r') as f:
    flag = True
    i = 0
    while flag:
        line = f.readline().split("\n")[0]
        domains.append(line)
        if len(line) <= 1:
            flag = False

ks = ["time", "domain", "noError", "totalCount", "aCount", "cnameCount", "mxCount", "txtCount", "clientipCount",
      "subdomainCount"]
ds = [" "] + generate_date_arr(4, 1, 6, 11)
tag = "totalCount-benign"
fi = tag

with open(fi + ".csv", "a") as f:
    for key in ds:
        f.write(key + ",")
    f.write("\n")

for domain in domains:
    with open(fi + ".csv", "a") as f:
        f.write(domain + ",")
        tfs = query_sld_traffic(domain, "20230401", "20230611")
        for tf in tfs:
            f.write(str(tf["totalCount"]) + ",")
        f.write("\n")
