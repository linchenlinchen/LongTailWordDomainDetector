import traceback
from config.db import DB
from config.log import Log

'''🌟-------------连接数据库----------------'''
db = DB()
logger = Log()

'''🌟-------------数据库操作----------------'''
def add_one_domain(table,info):
    try:
        mongo = db.get_mongo()['fraud_detection'][table]
        mongo.insert_one(info)
    except Exception as e:
        traceback.print_exc()

def get_all_domains_info(table):
    try:
        mongo = db.get_mongo()['fraud_detection'][table]
        domains = [x for x in mongo.find()]
        return domains
    except Exception as e:
        traceback.print_exc()

def update_one_domain(table,domain,aset):
    try:
        mongo = db.get_mongo()['fraud_detection'][table]
        mongo.update_one({"domain": domain}, {"$set": aset})
    except Exception as e:
        traceback.print_exc()