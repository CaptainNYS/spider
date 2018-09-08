import requests
from lxml import etree
import pymysql

conn=pymysql.connect(host='localhost',user='root',password='root',db='nys',port=3306,charset='utf8')#打开数据库连接，注意port字段类型为数字
cursor=conn.cursor()#创建一个游标对象

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
#获取详细信息函数
def get_info(url,page):
    user_id=url.split('/')
    user_id=user_id[4]
    if url.find('page='):
        page+=1
    html=requests.get(url,headers=headers)
    print(html.status_code)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        dd=info.xpath('div/div/div/span/@data-datetime')[0]
        #print(dd)
        type=info.xpath('div/div/div/span/@data-type')[0]
        cursor.execute("insert into nys_biao(date,typee) values(%s,%s)",(str(dd),str(type)))#执行sql语句
        conn.commit()  # 提交到数据库
    id_infos=selector.xpath('//ul[@class="note-list"]/li/@id')
    print(id_infos)
    if len(infos)>1:
        feed_id = id_infos[-1]
        max_id = int(feed_id.split('-')[1])-1
        next_url = 'http://www.jianshu.com/users/%s/timeline?max_id=%d&page=%s' % (user_id, max_id, page)
        get_info(next_url,page)

if __name__=='__main__':
    get_info('http://www.jianshu.com/users/9104ebf5e177/timeline',1)

