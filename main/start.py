import subprocess
import signal
import traceback

from spider_method.baidu_selenium_for_spider_pool import do_spider
from reverse_method.whois_reverse import do_reverse
from util.add_init_domains import add_init
from util.time.hander import set_timeout
set_timeout(do_spider,timeout=300)
set_timeout(add_init,timeout=7200)
set_timeout(do_reverse,timeout=72000)

def handler(signum, frame):
    # 定义一个信号处理函数，当超时发生时，触发该函数。
    raise TimeoutError("Function call timed out.")
signal.signal(signal.SIGALRM, handler)
# 设置超时时间
timeout = 30
signal.alarm(timeout)

try:
    # 执行函数调用
    result = do_spider()
    # 取消信号的设置
    signal.alarm(0)
except TimeoutError as te:
    try:
        timeout = 7200
        signal.alarm(timeout)
        add_init()
        # 取消信号的设置
        signal.alarm(0)
    except TimeoutError as te:
        try:
            timeout = 9600
            signal.alarm(timeout)
            do_reverse()
            # 取消信号的设置
            signal.alarm(0)
        except TimeoutError as te:
            print("timeout")
        except Exception as e:
            traceback.print_exc()
    except Exception as e:
        traceback.print_exc()
except Exception as e:
    traceback.print_exc()
# add_init()
# do_reverse()
