import requests
import json
import time
import random
headers={
    'Cookie':' ',#你的cookie信息
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36'
}
f=open('D:\\nys\study\projects\weibo2.txt','a+',encoding='utf-8')

def get_info(url,page): #定义获取信息函数
    html=requests.get(url,headers=headers)
    #print(html.status_code)
    json_data=json.loads(html.text)
    infos=json_data['data']['statuses']
    for info in infos:
        f.write(info['text'].split('<span')[0].split('<a')[0]+'\n')

    next_cursor=json_data['data']['next_cursor']
    time.sleep(1)

    if page < 5:
        next_url="https://m.weibo.cn/feed/circle?max_id={}".format(str(next_cursor))
        page+=1
        get_info(next_url,page)
    else:
        pass
        f.close()

if __name__=='__main__':
    url='https://m.weibo.cn/feed/circle?'
    get_info(url,1)