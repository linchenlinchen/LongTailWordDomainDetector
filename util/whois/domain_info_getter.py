'''第一步：获取域名IP'''
import socket
import sys
import urllib.request

hostname = "zhuandayup.cn"
ip = socket.gethostbyname(hostname)
print('Hostname: ', hostname, '\n' 'IP: ', ip)

'''第二步：获取域名状态.算了，要不直接用爬虫判断有没有'''
# res = urllib.request.urlopen("https://www.baidu.com")
# print(res.status)
from domainconnect import *
dc = DomainConnect()

'''第三步：找到同ip的其他domain'''

def domain_name(ip_addr):
  dom_name = socket.gethostbyaddr(ip_addr)
  print("The domain name for " + ip_addr + " is", dom_name)

ip_addr = "8.8.8.8"
domain_name(ip_addr)


