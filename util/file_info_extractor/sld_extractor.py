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

            urls = []
            for line in lines:
                #如果直接是域名
                if'http' not in line:
                    try:
                        sld = '.'.join(line.split(".")[-2:])
                    except Exception as e:
                        sld = ""
                else:
                    domain = line.split('/')[2]
                    sld = '.'.join(domain.split(".")[-2:])
                    if sld.startswith("com.cn"):
                        sld = '.'.join(domain.split(".")[-3:])
                urls.append(sld)
            # url匹配

            # pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
            # urls = re.findall(pattern, info)
            for u in urls:
                inners.add(u)
            #过滤
            d_s = set()
            special = {";","；","'",")","\"","?",",","/","\n",":","1","2","3","4","5","6","7","8","9","0"}
            inners_list = list(inners)
            for inner in inners_list:
                if inner is not None and ("alipay.com" in inner or "baidu.com" in inner or "tencent.com" in inner):
                    inners.remove(inner)
                if inner is not None and "/" not in inner and '.' in inner  and len(inner) > 5 and len(inner) < 25:
                    n = inner
                    if len(n) > 2:
                        while n[-1] in special:
                            n = n[0:-1]
                    # while ''.join(n[-2:]) == "\n":
                    #     n = n[0:-2]
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
        print(" " + n+ "000")
    return inners
if __name__ == "__main__":
    # extract_url("/Users/leenchardmen/Downloads/a3tcax6.cn跳转到m1mmlmm.j0xyhjz.buzz-百度游戏-0505.html")
    l = extract_url("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/reverse_method/draft.json")
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    j = 0
    k = 0
    for i in l:
        if ".buzz" in i:
            print(i,end="\t")
            c+=1
        if ".top" in i:
            d +=1
        if ".org" in i:
            e += 1
        if ".com.cn" in i:
            f += 1
        elif ".cn" in i:
            j += 1
        elif ".com" in i:
            k += 1
        if ".xyz" in i:
            g += 1
        if ".lol" in i:
            h += 1

    # print(len(extract_url("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/reverse_method/draft.json")))
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(j)
    print(k)