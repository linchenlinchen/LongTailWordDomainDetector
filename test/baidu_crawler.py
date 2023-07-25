import random
import time
import datetime
import traceback
from tqdm import *
import requests
from bs4 import BeautifulSoup
import sys
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import random
import filelock
import multiprocessing
starttime = datetime.datetime.now()
def get_baidu_search_result(keyword, ip,is_timeout=False):
    try:
        proxies = {
            "http": "" + ip,
            "https": "" +  ip
        }
        print(proxies)
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
        # results += soup.find_all('div', class_='result-op')
        di = {}
        for result in results:
            try:
                title = result.h3.text
                # print(title)
                di[title] = "ing"
            except Exception as e:
                traceback.print_exc()
    except:
        traceback.print_exc()
        if is_timeout:
            ip = get_ip()
            ip_pool.append(ip)
        else:
            ip = ip_pool[-2]
            time.sleep(5)
        
        return get_baidu_search_result(keyword, ip,True)
    return di


def error_log(word):
    print(" none!")
    with open("venv/data_bucket/err.txt", 'a') as e:
        e.write(word)


def get_ip():
    try:
        # return ""
        u = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
        
        # print(u)
        # u = "https://api.xiaoxiangdaili.com/ip/get?appKey=1000985058636877824&appSecret=GtqQAY2h&cnt=&wt=text"
        ip = requests.get(u)
        print(ip.text)
    except:
        traceback.print_exc()
        return ""
    return ip.text.split("\r\n")[0]
    return ip.text



def get_result(i,domains,ip,ip_pool,vectorizer,loaded_model):
    try:
        lock = multiprocessing.Lock()
        print(domains[i])
        endtime = datetime.datetime.now()
        if "starttime" not in locals():
            starttime = endtime
        print(str(endtime) + "," + str(starttime) + str((endtime - starttime).seconds))
        if (endtime - starttime).seconds >= 300:
            ip = get_ip()
            ip_pool.append(ip)
            # print(ip)
            # ip=""
            starttime = endtime
        di = get_baidu_search_result("site:"+domains[i], ip)
        print(di)
        
        with open("/Users/leenchardmen/Desktop/random1000titles.csv", 'a') as f:
            results = list(di.keys())
            if len(results) < 1:
                return
            # f.write(domains[i] + ",")
            X_new = vectorizer.transform([result.replace(" ","").replace("...","").replace("\n","") for result in results])
            predictions = loaded_model.predict(X_new)
            if 1 in predictions :
                lock.acquire()  # 请求锁
                f.write(domains[i] + ","+"True,"+results[0]+"\n")
                lock.release()  # 释放锁
            else:
                lock.acquire()  # 请求锁
                f.write(domains[i] + ","+"False\n")
                lock.acquire()  # 请求锁
            f.close()
    except:
        traceback.print_exc()
if __name__ == '__main__':
    starttime = datetime.datetime.now()
    # # 创建一个文件锁
    # lock = filelock.FileLock("/Users/leenchardmen/Desktop/random1000titles.csv")

    # 创建进程池
    pool = multiprocessing.Pool()
    ip_pool = []
    is_banned = False
    count = 0
    
    # time.sleep(10)
    # ip = get_ip()
    # with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/result_tubian_2000_0601.csv",'r') as f:
    #     domains = [x.split(",")[0] for x in f.readlines()]
    with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/test/result_tubian2000.csv","r") as f:
        domains = random.sample([x.split(",")[0] for x in f.readlines()], 1000)
    # 加载保存的模型
    with open("model.pickle", "rb") as f:
        loaded_model = pickle.load(f)

    # 准备数据集
    with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/match_title.csv",'r') as ps:
        positive_strings = [x.replace(" ","").replace("...","").replace("\n","") for x in ps.readlines()]
    with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/midmatch_title.csv",'r') as ms:
        middle_strings = [x.replace(" ","").replace("...","").replace("\n","") for x in ms.readlines()]
    with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/dismatch_title.csv",'r') as ns:
        negative_strings = [x.replace(" ","").replace("...","").replace("\n","") for x in ns.readlines()]

    positive_strings += middle_strings
    # 二分类
    random.shuffle(positive_strings)
    random.shuffle(negative_strings)
    print(positive_strings)
    X = positive_strings + negative_strings
    y = [1] * len(positive_strings) + [0] * len(negative_strings)

    # 准备数据集和标签
    text_data = X
    labels = y

    # 特征提取
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(text_data)
    y = labels

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 训练分类器
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)

    # 评估分类器
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    ip=get_ip()
    ip_pool.append(ip)
    # u = "https://api.xiaoxiangdaili.com/app/bindIp?appKey=1000985058636877824&appSecret=GtqQAY2h&cnt=&wt=text"
    # requests.get(u)
    for i in tqdm(range(len(domains))):
        pool.apply_async(get_result,args=(i,domains,ip,ip_pool,vectorizer,loaded_model,))
        
    # 关闭进程池，不再接受新的任务
    pool.close()

    # 等待所有任务完成
    pool.join()