# -*- coding: utf-8 -*-
# Captain_N


from lxml import etree
import random
import requests
import time
import pymysql   #导入相应库文件

conn = pymysql.connect(host='localhost',user='root',password='root',db='douban',port=3306,charset='utf8')
cursor=conn.cursor()    #连接数据库及光标
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}     #请求头



def get_info(url):
    res=requests.get(url,headers=headers)
    if res.status_code==200:
        selector=etree.HTML(res.text)
        infos=selector.xpath('//tr[@class="item"]')
        for info in infos:
            name=info.xpath('td/div/a/@title')[0]
            url=info.xpath('td/div/a/@href')[0]
            book_infos=info.xpath('td/p/text()')[0]
            author=book_infos.split('/')[0]
            publisher=book_infos.split('/')[-3]
            date=book_infos.split('/')[-2]
            price=book_infos.split('/')[-1]
            rate=info.xpath('td/div[@class="star clearfix"]/span[2]/text()')[0]
            comments=info.xpath('td/p/span/text()')
            if len(comments)!=0:
                comment=comments[0]
            else:
                comment='空'        #以上是获取电影详细信息
            cursor.execute("insert into doubanmovie(name,author,publisher,date,price,rate,comments) values(%s,%s,%s,%s,%s,%s,%s)",
                           (str(name),str(author),str(publisher),str(date),str(price),str(rate),str(comments)))     #按对应字段写入数据库

    else:
        print('failed')



if __name__=='__main__':     #主程序入口
    urls=['https://book.douban.com/top250?start={}'.format(i*25) for i in range(0,10)]     #构建需要爬去的页面连接
    #urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_info(url)  #调用爬去详细信息函数
        time.sleep(random.random()*2)
    conn.commit()
