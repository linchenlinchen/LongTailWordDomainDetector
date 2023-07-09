import random
import time
import requests
from bs4 import BeautifulSoup
import sys

sys.path.append("/Users/leenchardmen/PycharmProjects/malicicous_url_finder/venv/")

from config.db import DB
from config.log import Log

ip = "117.57.98.164:35537"

db = DB()
logger = Log()
table = 'baidu_search_result'
mongo1 = db.get_mongo()['fraud_detection'][table]
words = [x["keyword"] for x in mongo1.find()]


def add_one_word(info):
    try:
        mongo1.insert_one(info)
    except Exception as e:
        print("info['word']=" + info['word'] + ":error!")


def get_baidu_search_result(keyword,ip):
    proxies = {
        # "http": "http://" + ip,

    }
    url = 'https://www.baidu.com/s'
    params = {'wd': keyword}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        "Cookie": "PSTM=1660833817; BAIDUID=2721832B494F290028AC71DEC18B8501:FG=1; BIDUPSID=5078DA522A80F23B94D84796223ABB65; BD_UPN=123253; H_PS_PSSID=36558_38470_38440_38309_38468_38289_36804_38486_37931_38382_38356_26350_22159_37881; BA_HECTOR=8k0h0lal24810ha58k218gcu1i2l65u1n; BAIDUID_BFESS=2721832B494F290028AC71DEC18B8501:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=naVXOxGfri0BT8LPcAZN0x3BRxlouk:BniTISbfb3Z8c:C; SL_G_WPT_TO=zh; BD_CK_SAM=1; PSINO=1; delPer=0; COOKIE_SESSION=456_0_9_9_5_23_0_0_8_9_1_5_10390_0_0_0_1680253741_0_1680513670|9#351105_45_1679424425|9; ab_sr=1.0.1_YmVjNjMxZjdlMTIyOWUwNTdjMGIwMTJhMTY3MjEzNDVmN2ZhZTM5MDAzZjg3MWYzNGM2MDM5NDhiMGRjZmM5OWYwOTIyMDQ4YTgzMTg2ODI1NmU3Zjg4NGUxOTdiYjA4ZjczNWVmY2EyZWI3NGFiYWQwZGQ4NWVjNjI4MTQyOTY5ZmYzNDE0YzQ3NTU4N2FjNWU2OGUyZWEzN2IzZGQ3NA==; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; H_PS_645EC=ea39y/F/aVwkp2xlVkEB5C7Z5ykV9HRi886WunDPyaxLuWmZcKHZcL0NAAs"
    }
    # 常见的 user-agent 列表
    headers_list = [
        {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
        }, {
            'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
        }, {
            'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
        }, {
            'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
        }, {
            'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
        }, {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        }, {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }, {
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
        }
    ]
    headers = random.choice(headers_list)
    response = requests.get(url, params=params, headers=headers, proxies=proxies, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='result')
    results += soup.find_all('div', class_='result-op')
    di = {}
    for result in results:
        try:
            title = result.h3.a.text
            link = result.h3.a['href']
            di[title] = link
        except Exception as e:
            pass
    return di


def error_log(word):
    print(" none!")
    with open("venv/data_bucket/err.txt", 'a') as e:
        e.write(word)

def get_ip():
    u = "https://api.xiaoxiangdaili.com/ip/get?appKey=959018537719320576&appSecret=CbIyAqnZ&cnt=&wt=text"
    ip  = requests.get(u)
    return ip.text
import datetime
if __name__ == '__main__':
    is_banned = False
    count= 0
    starttime = datetime.datetime.now()
    with open('venv/data_bucket/generated_keyword.txt', 'r') as fp:
        while True:
            try:
                endtime = datetime.datetime.now()
                if (endtime - starttime).seconds > 180:
                    ip = get_ip()
                    starttime = endtime
                if not is_banned or count > 8:
                    keyword = fp.readline()
                    count = 0
                print(keyword)
                if keyword in words:
                    continue
                di = get_baidu_search_result(keyword,ip)
                time.sleep(3 + random.random() * 3)
                if len(di.keys()) < 1:
                    # time.sleep(5 + random.random() * 10)
                    # error_log(keyword)
                    # is_banned = True
                    # count += 1
                    continue
                add_one_word({"keyword": keyword, "info_list": di})
                is_banned = False
                print(keyword + ":OK!")
            except:
                print("error!")
