# -*- coding: utf-8 -*-
# Captain_N
#urls=['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i))for i in range(1,24)]

import requests
from bs4 import BeautifulSoup
import time

headers={'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 '}
def get_info(url):
    Response = requests.get(url,headers=headers)
    soup=BeautifulSoup(Response.text,'lxml')
    ranks=soup.select('span.pc_temp_num')
    titles=soup.select(' div.pc_temp_songlist > ul > li > a')
    print(titles)
    times=soup.select(' span.pc_temp_tips_r > span')
    for rank,title,time in zip(ranks,titles,times):
        data={
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(data)
if __name__=='__main__':
    urls=['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i))for i in range(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(1)
