import codecs
import csv
import sys
import traceback

sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/")

from db import DB
from log import Log

db = DB()
logger = Log()
table = 'baidu_fraud_info'
mongo1 = db.get_mongo()['fraud_detection'][table]


def add_one_word(info):
    try:
        mongo1.insert_one(info)
    except Exception as e:
        print(":error!")


if __name__ == '__main__':
    datas = []
    with codecs.open('/Users/leenchardmen/PycharmProjects/malicicous_url_finder/analysis/test.csv',
                     encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            datas.append(row)
    f.close()
    print(datas)
    urls = []
    urls_dict = {}
    keywords = []
    keywords_dict = {}
    domains = []
    domains_dict = {}
    domain_keywords_map = {}
    keywords_domain_map = {}
    for data in datas:
        urls.append(data['跳转域名'])
        if data['跳转域名'] in urls_dict.keys():
            urls_dict[data['跳转域名']] += 1
        else:
            urls_dict[data['跳转域名']] = 1
        keywords.append(data['搜索词'])
        if data['搜索词'] in keywords_dict.keys():
            keywords_dict[data['搜索词']] += 1
        else:
            keywords_dict[data['搜索词']] = 1

        if data['跳转域名'] == '':
            domain = 'null'
        elif len(data['跳转域名'].split('/')) < 3:
            domain = data['跳转域名']
        else:
            domain = data['跳转域名'].split('/')[2]

        domains.append(domain)
        if domain in domains_dict.keys():
            domains_dict[domain] += 1
        else:
            domains_dict[domain] = 1
        if domain in domain_keywords_map.keys():
            domain_keywords_map[domain].add(data['搜索词'])
        else:
            s = set()
            s.add(data['搜索词'])
            domain_keywords_map[domain] = s
        if data['搜索词'] in keywords_domain_map.keys():
            keywords_domain_map[data['搜索词']].add(domain)
        else:
            s = set()
            s.add(domain)
            keywords_domain_map[data['搜索词']] = s
    # l = sorted(keywords_dict.items(), key=lambda kv: (kv[1], kv[0]))
    # d = {}
    # for i in l:
    #     d[i[0]] = i[1]
    # add_one_word(d)
    # l = sorted(domains_dict.items(), key=lambda kv: (kv[1], kv[0]))
    # d = {}
    # for i in l:
    #     d[i[0]] = i[1]
    # add_one_word(d)
    # l = sorted(urls_dict.items(), key=lambda kv: (kv[1], kv[0]))
    # d = {}
    # for i in l:
    #     d[i[0]] = i[1]
    # add_one_word(d)
    # for domain in domain_keywords_map.keys():
    #     domain_keywords_map[domain] = list(domain_keywords_map[domain])
    for keyword in keywords_domain_map.keys():
        keywords_domain_map[keyword] = list(keywords_domain_map[keyword])
    print("ahhhh---")
    print(keywords_domain_map)
    add_one_word(keywords_domain_map)
    # add_one_word(domains_dict)
