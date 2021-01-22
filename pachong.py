# -*- encoding: utf-8 -*-
import urllib.request as ur
from bs4 import BeautifulSoup
import requests
import time
while True:
    addr="http://neunews.neu.edu.cn/tzgg/list.htm"
    key="http://sc.ftqq.com/[SCKEY].send?"   #替换你的SCKRY
    res = ur.urlopen(addr)
    soup = BeautifulSoup(res, "html.parser")
    aAll = soup.select("div[frag='面板89'] .news_list a")
    first=aAll[0].text
    while True:
        try:
            res=ur.urlopen(addr)
            soup=BeautifulSoup(res,"html.parser")
            aAll=soup.select("div[frag='面板89'] .news_list a")
            if aAll[0].text!=first:
                link="http://neunews.neu.edu.cn/"+aAll[0]["href"]
                text=key+"text="+first+"&desp="+link
                post=requests.post(text)
                print("已发送消息",aAll[0].string,"!")
                first = aAll[0].text
            else:
                print("无变化！")
            time.sleep(500)
        except:
            print("出错了，重来！")
