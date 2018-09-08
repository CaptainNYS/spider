# -*- coding: utf-8 -*-
# Captain_N
##########间歇性报keyerror#############
import requests
import  csv
from lxml import etree
import json
import random
import time

headers={'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400'

}
info_url='https://www.qiushibaike.com'
def get_user_url(url):
        res=requests.get(url,headers=headers)
        info=etree.HTML(res.text)
        user_urls=info.xpath('//div[@class="author clearfix"]/a[2]/@href')
        for url in user_urls:
            if url:
                url=info_url+url
                get_address(url)
            else:
                pass

def get_address(url):

    res=requests.get(url,headers=headers)
    info=etree.HTML(res.text)
    address=info.xpath('//div[@class="user-col-left"]/div[2]/ul/li[4]/text()')
    #//html/body/div[3]/div/div[3]/div[2]/ul/li[4]/text() 用浏览器与上述xpath相同，但是返回为空表，mmp
    if address:
        get_geo(address)
    else :
        pass
def get_geo(address):
    geo=address[0].split('·')[0].strip()
    url = 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address=' + str(geo)
    #http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address=石家庄
    res = requests.get(url)
    json_data=json.loads(res.text)
    if (json_data['result']):
        try:
            lon = float(json_data['result']['location']['lng'])
            lat = float(json_data['result']['location']['lat'])
            with open('E:\爬虫\projects\map\map.csv', 'a+', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow((geo,lon,lat))
        except Exception:
            print('failed')
    else:
        pass

if __name__=="__main__":
    urls=['https://www.qiushibaike.com/8hr/page/{}'.format(str(i)) for i in range(1,11)]
    print(urls)
    with open('E:\爬虫\projects\map\map.csv','wt',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(('address','longtitude','latitude'))
        i=1
    for url in urls:
        print('爬取第'+str(i)+'页')
        get_user_url(url)
        time.sleep(random.random()/2)
        i+=1


