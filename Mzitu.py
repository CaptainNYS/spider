# -*- coding: utf-8 -*-
# Captain_N
########################失败,见Mzitu2.py############################
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time
import random
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
}
download_links=[]
path='e:/爬虫/projects/img/'
url='http://www.mzitu.com/'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')
imgs=soup.select('#picture  p  a  img')

#sidebar > div.hotpic.clearfix > ul > li:nth-child(10) > a > img
##picture > p > a > img

for img in imgs:
    print(img.get('src'))
    download_links.append(img.get('src'))
i=1
for item in download_links:
    urlretrieve(item,path+item[-10:])
    print('获取第'+str(i)+'张')
    i+=1
    time.sleep(random(0.1,0,3))
    if i>=2:
        break
