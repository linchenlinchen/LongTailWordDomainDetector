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
from util.database.impl.database_impl import add_one_domain_impl
from util.database.impl.database_impl import get_all_domains_info_impl
from util.database.impl.database_impl import db
from util.whois.whois_get_registrant_info import get_whois
from util.database.impl.database_impl import table
from util.code_info_extractor.get_sld_from_url import get_sld
from config.db import DB
from config.log import Log
from util.whois.whois_get_registrant_info import query_filtered_whois_detail, query_whois_by_email
from util.network.connection_test import shrink_domain

def do_reverse():
    sys.setrecursionlimit(30000)
    # 利用注册人信息反查部分
    # tag = "email"
    # db = DB()
    # logger = Log()
    # table = 'domains_from_' + tag
    # mongo1 = db.get_mongo()['fraud_detection'][table]
    # ks = set([i[tag] for i in mongo1.find()])
    # # 0510
    # datas = [
    #     'qifengshan2022@163.com', '287446996@qq.com', 'yy17143310875@163.com', 'qinghuandu202206@163.com', 'HfcgfC.com@NameBrightPrivacy.com', 'caihunfe51111@163.com', 'qq340080738@163.com', '1099221484@qq.com',   'muskseo1971@gmail.com', 'b0702086@163.com', 'lielierng665888@163.com', 'dp1pkrrn@163.com', '1465483853@qq.com', '510440879@qq.com', 'zxdds13086714461@163.com', 'cpfwmsx@126.com', 'nttuwerw18@2021221.com', 'xialan2824@sohu.com', '66517379@qq.com', 'maidaoxindong@163.com', 'nh93573314huiche@163.com', 'golinkkele@163.com', 'achilles2325213@gmail.com', 'info@heyou51.com', 'mm19808226591@163.com', '3361645342@qq.com', 'wang6668899@gmail.com', '13915351337@139.com', '1557591262@qq.com', 'golinkyuzai@163.com'
    # ]

    emails = set([x["email"] for x in get_all_domains_info_impl(table, type=None, has_email=True)])
    # emails = {"751066209@qq.com"}
    print(emails)
    for email in emails:
        try:
            related_domains = query_whois_by_email(email, False)
            print(len(related_domains))
            # for related_domain in related_domains:
            #     if
            i = 0
            print(shrink_domain(related_domains))
            for related_domain in related_domains:
                print(str(i), end="\t")
                i += 1
                info = query_filtered_whois_detail(related_domain)
                add_one_domain_impl(table, related_domain, type="whois", check=False, email=info["registrantEmail"][0],
                                    name=info["registrantOrganization"][0], phone=info["registrantOrganization"][0],
                                    org=info["registrantOrganization"][0], from_email=email,
                                    is_seed=True)
        except:
            traceback.print_exc()
    # ll = 0
    # for data in datas:
    #     info = {tag: data}
    #     # 替换函数
    #     domains_list = who.query_whois_by_email(data)
    #     info["domains_list"] = list(set(domains_list))
    #     ll += len(list(set(domains_list)))
    #     if data not in ks:
    #         add_one_word(info)
    # print(ll)


# do_reverse()
