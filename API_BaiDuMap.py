# -*- coding: utf-8 -*-
# Captain_N
############书上url返回数据不正常#################
import requests
import pprint
import json
from lxml import etree
from bs4 import BeautifulSoup

address = input('地点：')
url= 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address='+str(address)
##################书上这个url不能正常返回信息#####################url='http://restapi.amap.com/v3/geocode/geo'

html=requests.get(url)
# print(html.text)
######json
info=json.loads(html.text)
print(info)
print(float(info['result']['location']['lat']))
print(float(info['result']['location']['lng']))


# address = input('地点：')
# url= 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&address='+str(address)
# response = requests.get(url)
# print(response.text)
# answer = response.json()
# print(answer)
# lon = float(answer['result']['location']['lng'])
# lat = float(answer['result']['location']['lat'])
# print(lon,lat)