import sys
sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/config")
from config.db import DB
db = DB()
#--------------------
spider_begin = "haoyangsoft.com"
table = 'baidu_'+spider_begin+'_result'
mongo1 = db.get_mongo()['fraud_detection'][table]
domains_raw = {x["url"] for x in mongo1.find()}
special = {"com.cn","net.cn","net.com",'gov.cn'}
l = set()
for i in domains_raw:
    if len(i.split("/")[2].split(".")) == 2:
        l.add(i.split("/")[2])
    elif len(i.split("/")[2].split(".")) >= 3 and '.'.join(i.split("/")[2].split(".")[-2:]) not in special:
        l.add('.'.join(i.split("/")[2].split(".")[-2:]))
    elif len(i.split("/")[2].split(".")) >= 3:
        l.add('.'.join(i.split("/")[2].split(".")[-3:]))
    else:
        l.add(i)
print(l)
print(len(l))