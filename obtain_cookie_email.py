import selenium
from selenium import webdriver
import time#用来等待网页反应
import re#用来获取html中ip的位置
option=webdriver.ChromeOptions()
option.add_argument('headless') # 设置option
driver = webdriver.Chrome(chrome_options=option)

# driver = webdriver.Chrome()
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip%E6%9F%A5%E8%AF%A2")
text=driver.page_source
location=re.search('本机IP:',text).span()[0]#正则
text=text[location:location+40]
#百度搜索“IP查询”并获取ip保存为text

driver.get("https://mail.qq.com/")
driver.switch_to.frame("login_frame")
driver.find_element_by_xpath('//*[@id="qlogin_list"]/a[1]').click()
time.sleep(5)#点击快速登陆并等待五秒
driver.find_element_by_xpath('//*[@id="composebtn_td"]').click()
cookie = driver.get_cookies()
cookie_string=str(cookie)
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys("1624910298@qq.com")
driver.find_element_by_xpath('//*[@id="subject"]').send_keys(text)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@class="qmEditorIfrmEditArea"]'))
driver.find_element_by_xpath('/html/body').send_keys(cookie_string)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_id('mainFrame'))
driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
time.sleep(10)
driver.quit()



# #
# driver.switch_to.default_content()
# driver.switch_to.frame("login_frame")
# driver.switch_to.frame("tcaptcha_iframe")
# #






# driver.switch_to.default_content()
# driver.switch_to.frame("login_frame")
# driver.switch_to.frame("tcaptcha_iframe")
# print(driver.current_url)
# # text=driver.page_source
# cookie = driver.get_cookies()



# get_cookies()     　　            获得cookie信息

# driver.add_cookie(cookie)        添加cookie

# delete_cookie(name)             删除特定(部分)的cookie

# driver.delete_all_cookies()              删除所有的cookie












