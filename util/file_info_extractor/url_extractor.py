import traceback
from selenium.webdriver.common.by import By
import sys

sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/")
import re
from db import DB
from log import Log
def extract_url(file_path):
    inners = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # 读取所有行
            lines = f.readlines()
            info = ""
            for line in lines:
                info += line
            # url匹配
            pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
            urls = re.findall(pattern, lines)
            for u in urls:
                inners.add(u)
            #过滤
            d_s = set()
            special = {";","；","'",")","\"","?",","}
            inners_list = list(inners)
            for inner in inners_list:
                if inner is not None and ("alipay.com" in inner or "baidu.com" in inner or "tencent.com" in inner):
                    inners.remove(inner)
                if inner is not None and "http" in inner:
                    n = inner
                    while n[-1] in special:
                        n = n[0:-1]
                    if len(n) < len(inner):
                        inners.add(n)
                        inners.remove(inner)
                else:
                    inners.remove(inner)
            for inner in inners:
                try:
                    if inner.endswith(")") or inner.endswith(".css") or inner.endswith(".gif") or inner.endswith(".png") or inner.endswith(".jpg") or inner.endswith(".js") or inner.endswith(".mp3") or inner.endswith(".mp4") or inner.endswith(".avi") or inner.endswith(".wmv") or inner.endswith(".mpg") or inner.endswith(".mpeg") or inner.endswith(".mov") or inner.endswith(".swf”") or inner.endswith(".flv") or inner.endswith(".rm”") or inner.endswith(".ram"):
                        d_s.add(inner)
                except Exception:
                    traceback.print_exc()
                    print("**************"+str(inners))
                    print("&&&&&&&&&&&&&&&&"+str(inner))
            inners.difference_update(d_s)
            print(inners)
    except Exception as e:
        traceback.print_exc()
    return inners
if __name__ == "__main__":
    # extract_url("/Users/leenchardmen/Downloads/a3tcax6.cn跳转到m1mmlmm.j0xyhjz.buzz-百度游戏-0505.html")
    extract_url("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/reverse_method/draft.json")