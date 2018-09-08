from selenium import  webdriver
from lxml import  etree
import time
import pymysql
import random

conn = pymysql.connect(host='localhost',user='root',password='root',db='jingdong',port=3306,charset='utf8')
cursor=conn.cursor()    #连接数据库及光标
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}     #请求头
driver=webdriver.Chrome()#实例化浏览器
driver.maximize_window()

def NextPage(url,page):

    #driver.get(driver.current_url)#此处参数必须为current-url
    driver.get(url)#不能用URL，URL在入口程序中赋值为京东首页
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('pn-next').click()
    # driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
    time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/input').clear()#模拟修改下一页,//*[@id="J_bottomPage"]/span[2]/input
    # driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/input').send_keys('%d' % page)
    # driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/a').click()#//*[@id="J_bottomPage"]/span[2]/a
    # time.sleep(2)
    driver.get(driver.current_url)#请求模拟点击后的URL
    driver.implicitly_wait(10)
    get_info(driver.current_url,page)

def get_info(url,page):
    page += 1
    driver.get(url)
    driver.implicitly_wait(10)#隐式等待10s，time.sleep是绝对的时间，设置长了浪费时间，设置短了没法解释完JavaScript，而implicitly_wait()函数是智能等待，解释完JavaScript后就会进入下一步，不浪费时间
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for i in range(50):
        js = 'window.scrollBy(0,100)'
        driver.execute_script(js)
        time.sleep(0.25)
    #time.sleep(5)
    selector=etree.HTML(driver.page_source)#请求网页源码
    infos=selector.xpath('//*[@id="J_goodsList"]/ul/li/div')
    a=len(infos)
    for info in infos:
        name = info.xpath('div[3]/a/em/text()[1]')[0]
        config = info.xpath('div[3]/a/em/text()[2]')
        if len(config)==0:
            config='null'
        else:
            config=config[0]
        price=info.xpath('div[2]/strong/i/text()')[0]
        comm_num=info.xpath('div[4]/strong/a/text()')[0]
        if len(comm_num)==0:
            comm_num='null'
        else:
            pass
        shop=info.xpath('div[5]/span/a/text()')
        if len(shop)==0:
            shop='null'
        else:
            shop=shop[0]
        cursor.execute(
            "insert into jingdong(name,price,config,comm_num,shop) values(%s,%s,%s,%s,%s)",
            (str(name), str(price), str(config), str(comm_num), str(shop)))  # 按对应字段写入数据库
        conn.commit()
    if page<=20:
        NextPage(url,page)
    else:
        pass

if __name__=='__main__':
    page = 1
    url='https://www.jd.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('key').clear()#注意必须是可更改的input元素的位置
    driver.find_element_by_id('key').send_keys('笔记本电脑')
    driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
    time.sleep(2)
get_info(driver.current_url, page)#笔记本电脑第一页