# -*- coding: utf-8 -*-
# Captain_N
########################失败#############################
import  requests
from bs4 import BeautifulSoup
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}

def get_links(url):
    res1 = requests.get('http://bj.xiaozhu.com/', headers=headers)
    print(res1)
    soup = BeautifulSoup(res1.text, 'lxml')
    links=soup.select('#page_list > ul > li > a')
    for link in links:
        href=link.get('href')
        # try:
        get_info(href)
        # except:
        #     print('failed')
        time.sleep(0.5)

def get_info(url):
    res2= requests.get(url,headers= headers)
    print(res2)
    soup=BeautifulSoup(res2.text,'lxml')
    titles=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    addresses=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    prices=soup.select('#pricePart > div.day_l > span')
    names=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for title,address,price,name,sex in zip(titles,addresses,prices,names,sexs):
        data={
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text().strip(),
            'name':name.get_text().strip(),
            'sex':judgement_sex(sex.get('class'))
        }
        print(data)
def judgement_sex(class_name):
    if class_name == ['member_icol']:#因为sex.get('class')返回的是列表形式
        return '女'
    else:
        return '男'

if __name__=='__main__':
    urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(2,3)]
    urls.insert(0,'http://bj.xiaozhu.com')
    for url in urls:
        get_links(url)
        time.sleep(1)

