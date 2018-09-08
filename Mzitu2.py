# -*- coding: utf-8 -*-
# Captain_N
####################煎蛋网  动态加载网站普通方法不起作用############################
# import requests
# from lxml import etree
# from bs4 import BeautifulSoup
# urls=['http://jandan.net/ooxx/page-{}#comments'.format(i) for i in range (0,2)]
# path='e:/爬虫/projects/img/'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
# }
#
#  #BeautifulSoup
# def get_info(url):
#     res=requests.get(url,headers=headers)
#     soup=BeautifulSoup(res.text,'lxml')
#     photo_urls=soup.select(' div.text p img')
#     i=0
#     for photo_url in photo_urls:
#         i+=1
#         photo=photo_url.get('src')
#         res=requests.get(photo,headers=headers)
#         with open(path+i+'jpg','wb') as f:
#             f.write(requests.get(photo).content)
#
#
# for url in urls:
#     get_info(url)

from bs4 import BeautifulSoup
import requests
##comment-3906004 > div > div > div.text > p > img
url  = 'http://jandan.net/ooxx'

wb_html = requests.get(url)
soup = BeautifulSoup(wb_html.text,'lxml')
imgs = soup.select('.text p img')
pic_id = 0
for img in imgs:
    img_url = img.get('src')
    pic_file = open('./pic_'+str(pic_id)+'.jpg','wb')
    pic_file.write(requests.get(img_url).content)
    pic_id=pic_id+1
    pass

############县长写的可以爬下来妹子图网照片

# from bs4 import BeautifulSoup
# import requests
#
# url  = 'http://www.meizitu.com/'
#
# wb_html = requests.get(url)
# soup = BeautifulSoup(wb_html.text,'lxml')
# imgs = soup.select('#picture p a img')
# pic_id = 0
# for img in imgs:
#     img_url = img.get('src')
#     pic_file = open('./pic_'+str(pic_id)+'.jpg','wb')
#     pic_file.write(requests.get(img_url).content)
#     pic_id=pic_id+1
#     pass


