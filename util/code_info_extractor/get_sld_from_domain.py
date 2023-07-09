m = set()
special = {"com.cn","net.cn","net.com",'gov.cn'}
domains =['www.zhjunjia.cn', 'wpa.b.qq.com', 'www.ximengnaikang.com', 'wpd.b.qq.com', 'zc.116.chstar.com.cn', 'shssj.net', 'm.operation.hospitalkowloon.com', 'www.kiavid.com', 'yyh.ceo120.net', 'm.doctor.shqianlx.com', 'baoshcn.com', 'www.qdtmjgjt.com', 'service-f1qklf7o-1317007870.hk.apigw.tencentcs.com', 'www.nblvdong.com', 'zsyycrz.com', 'lizhelawyer.com', 'www.weldelite.cn', 'www.yizhaobiao.net', 'flk.youhuangou.com', 'ld.jspyhb.com', 'jiaofu.sdkuma.com', 'dlunitedmining.com', 'demomarket.jisujsq.com', 'www.hkyzz.net', 'www.kaopu001.com', 'xmnk.cn', 'www.na-do.com', 'www.fhyhy.com', 'wpl.b.qq.com', 'www.huezk.com', 'www.jsnjdz.com', 'www.long120.net', 'www.xlxq66.com', 'www.huahaiweb.com', 'www.woqichuxing.cn', '4g.long120.net', 'atoom.cthysq.cn', 'qsjt.youhuangou.com', 'monluxe.cn', 'www.zemakeji.com', 'www.dyshengtong.com', 'demo.intspire.net', 'www.haodewj.cn', 'www.jzltzfw.com', '6g.shjiulong.cn', 'www.scslk.com']
for domain in domains:
    if len(domain.split(".")) >= 3 and '.'.join(domain.split(".")[-2:]) not in special:
        m.add(".".join(domain.split(".")[-2:]))
    elif len(domain.split("."))>=3:
        m.add(".".join(domain.split(".")[-3:]))
    elif len(domain.split("."))==2:
        m.add(domain)
print(list(m))
print(len(m))
