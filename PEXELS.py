# -*- coding: utf-8 -*-
# Captain_N
################默认加载15张，其余是动态加载#############
import requests
from bs4 import BeautifulSoup
import time
import random

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}
path='e:/爬虫/projects/img/'
word=input('catagories:')
url='https://www.pexels.com/search/'+word

res=requests.get(url)
soup=BeautifulSoup(res.text,'lxml')
imgs=soup.select('article > a > img')
list=[]
for img in imgs:
    photo=img.get('src')
    list.append(photo)
i=1
for item in list:
    data=requests.get(item,headers=headers)
    print('获取第'+str(i)+'张')
    i+=1
    time.sleep(random.random()/2)
    f=open(path+item.split('?')[0][-10:],'wb')
    f.write(data.content)
    f.close()