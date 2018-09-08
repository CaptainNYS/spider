# -*- coding: utf-8 -*-
# Captain_N
import re
import requests
import time

headers={
    'UserAgent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
}

f = open('E:\爬虫\projects\doupo.txt','a+')

def get_text(url):
 res = requests.get(url, headers=headers)
 if res.status_code==200:
    contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
    for content in contents:

        content1 = re.sub('&ldquo;','“',content)
        content2 = re.sub('&rdquo;', '”', content1)
        content3=re.sub('^天才一秒记住本站.*','',content2)
        new_content=re.sub('&hellip','...',content3)
        print(new_content)
        f.write(new_content.strip()+'\n')
 else:
     pass

if __name__=='__main__':
 urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,10)]
 for url in urls:
     get_text(url)
     time.sleep(0.5)

f.close()
