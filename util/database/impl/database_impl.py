import traceback

from util.database.template.database_template import db
from util.database.template.database_template import add_one_domain
from util.database.template.database_template import get_all_domains_info
from util.database.template.database_template import update_one_domain

'''计算当天日期的月、日'''
import datetime

current_date = datetime.date.today()
current_month = current_date.month
current_day = current_date.day
current_time = datetime.datetime.now()

table = "A_Long_Tail_Domain_" + str(current_month) + "_" + str(current_day)


def add_one_domain_impl(table, domain, type, check, email, name, phone, org,from_email=None, is_seed=False, time=datetime.datetime.now()):
    all = get_all_domains_info(table)
    domains = [x["domain"] for x in all]
    '''待加入待domain已经加入过，只能更新'''
    if domain in domains:
        try:
            if type == "spider":
                if from_email is not None:
                    update_one_domain(table, domain,
                                      {"domain": domain, "time": time, "type": type, "check": check, "email": email,
                                       "name": name, "phone": phone, "org": org, "from_email": from_email})
                else:
                    update_one_domain(table, domain,
                                      {"domain": domain, "time": time, "type": type, "check": check, "email": email,
                                       "name": name, "phone": phone, "org": org})
            else:
                if from_email is not None:
                    update_one_domain(table, domain,
                                  {"domain": domain, "time": time, "check": check, "email": email,
                                   "name": name, "phone": phone, "org": org, "from_email": from_email})
                else:
                    update_one_domain(table, domain,
                                      {"domain": domain, "time": time, "check": check, "email": email,
                                       "name": name, "phone": phone, "org": org})
        except Exception as e:
            traceback.print_exc()
    else:
        '''正常添加'''
        try:
            add_one_domain(table,
                           {"domain": domain, "time": time, "type": type, "check": check, "email": email, "name": name,
                            "phone": phone, "org": org, "is_seed":is_seed, "from_email": from_email})
        except Exception as e:
            traceback.print_exc()


def get_all_domains_info_impl(table, type=None, has_email=None):
    try:
        mongo = db.get_mongo()['fraud_detection'][table]
        if type is not None:
            if has_email:
                domains = [x for x in mongo.find() if x["type"] == type and len(x["email"]) > 5]
            else:
                domains = [x for x in mongo.find() if x["type"] == type]
        else:
            if has_email:
                domains = [x for x in mongo.find() if len(x["email"]) > 5]
            else:
                domains = [x for x in mongo.find()]
        return domains
    except Exception as e:
        traceback.print_exc()