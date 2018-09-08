# -*- coding: utf-8 -*-
# Captain_N
#https://www.jianshu.com/c/bDHhpK?order_by=commented_at&page=2

import requests
import time
import random
from lxml import etree
import pymysql
import multiprocessing
conn = pymysql.connect(host='localhost',user='root',password='1234',db='jianshu',port=3306,charset='utf8')
cursor=conn.cursor()    #连接数据库及光标

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}     #请求头


def get_info(url):
    try:#获取详细信息
        res=requests.get(url,headers=headers)
        time.sleep(random.random()/2)
    except Exception:
        pass
    if (res.status_code==200):
        html=etree.HTML(res.text)
        infos=html.xpath('//ul[@class="note-list"]/li/div')
        try:
            for info in infos:
                title=info.xpath('a/text()')[0]
                author=info.xpath('div/a/text()')[0]
                comment=info.xpath('div/a[2]/text()')[1].strip()
                like=info.xpath('div/span/text()')[0].strip()
                sponsor=info.xpath('div/span[2]/text()')
                if len(sponsor)==0:
                    sponsor='无'
                else:
                    sponsor=sponsor[0].strip()
                cursor.execute("insert into JianShu_Info(title,author,comment,like_num,sponsor) values (%s,%s,%s,%s,%s)",
                               (str(title),str(author),str(comment),str(like),str(sponsor)))     #按对应字段写入数据库
                conn.commit() #注意提交！！！！！！！
        except Exception:
            pass

if __name__=='__main__':
    urls=['https://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(str(i)) for i in range(1,1001)]
    pool=multiprocessing.Pool(processes=4)
    pool.map(get_info,urls)
