from selenium import  webdriver       #导入库
driver=webdriver.Chrome()             #指定浏览器
driver.get('https://www.douban.com/')  #
driver.implicitly_wait(10)             #隐式等待
driver.find_element_by_id('form_email').clear() #清除输入框数据
driver.find_element_by_id('form_email').send_keys('')  #输入账号
driver.find_element_by_id('form_password').clear()
driver.find_element_by_id('form_password').send_keys('')#输入密码
driver.find_element_by_class_name('bn-submit').click()  #单机登陆
print(driver.page_source)

#hosts需要添加 127.0.0.1 localhost