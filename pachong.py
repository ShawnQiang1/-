# -*- encoding: utf-8 -*-
import urllib.request as ur
from bs4 import BeautifulSoup
import requests
import time
addr="http://neunews.neu.edu.cn/tzgg/list.htm"
key="http://sc.ftqq.com/[SCKEY].send?"
res = ur.urlopen(addr)
soup = BeautifulSoup(res, "html.parser")
aAll = soup.select("div[frag='面板89'] .news_list a")
first=aAll[0].string
while True:
    res=ur.urlopen(addr)
    soup=BeautifulSoup(res,"html.parser")
    aAll=soup.select("div[frag='面板89'] .news_list a")
    if aAll[0].string!=first:
        first=aAll[0].string
        link="http://neunews.neu.edu.cn/"+aAll[0]["href"]
        text=key+"text="+first+"&desp="+link
        post=requests.post(text)
        print("已发送消息",aAll[0].string,"!")
    else:
        print("无变化！")
    time.sleep(5)
