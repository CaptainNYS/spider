# -*- coding: utf-8 -*-
# Captain_N


from lxml import etree
import csv
import requests
import time   #导入相关的库


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}   #请求头

fp=open('E:\爬虫\projects\DouBan250.csv','wt',newline='',encoding='utf-8')   #创建Excel文件
writer=csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))   #创建csv，写入表头

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
                comment='空'      #以上为获取详细信息
            writer.writerow((name,url,author,publisher,date,price,rate,comment))    #按对应的表头写入数据

    else:
        print('failed')



if __name__=='__main__':  #主程序入口
    urls=['https://book.douban.com/top250?start={}'.format(i*25) for i in range(0,10)]
    #urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_info(url)
        time.sleep(1)
fp.close()#关闭csv文件
