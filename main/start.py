import subprocess

from spider_method.baidu_selenium_for_spider_pool import do_spider
from reverse_method.whois_reverse import do_reverse

from util.time.hander import set_timeout
# set_timeout(do_spider,timeout=300)
# set_timeout(do_reverse,timeout=7200)
do_reverse()
