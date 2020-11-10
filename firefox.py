#firefox不如chrome
# 进入浏览器设置
import PIL
from PIL import Image
import selenium
from selenium import webdriver
from io import BytesIO
import requests
#import cv2
import time
import numpy as np
#输入账号和密码
#account=input()
#password=imput()
account='1099653018'
password=123456



driver = webdriver.Firefox()
driver.get("https://mail.qq.com/")
driver.switch_to.frame("login_frame")
driver.find_element_by_id('switcher_plogin').click()#默认快速登陆 点击进入账号密码登录
a=driver.find_element_by_xpath('//*[@id="u"]')
a.send_keys(account)
a=driver.find_element_by_xpath('//*[@id="p"]')
a.send_keys(password)
a=driver.find_element_by_xpath('//*[@id="login_button"]')
time.sleep(0.1)
a.click()#回车


#
driver.switch_to.default_content()
driver.switch_to.frame("login_frame")
driver.switch_to.frame("tcaptcha_iframe")
#

'''
本来想寻找暗块的 后发现qq邮箱的暗块都在右边且可以多次移动

本来想寻找暗块的 后发现qq邮箱的暗块都在右边且可以多次移动

本来想寻找暗块的 后发现qq邮箱的暗块都在右边且可以多次移动
遂采取遍历
# a=driver.find_elements_by_class_name("tc-bg")
# a=driver.find_element_by_id('slideBg')
a=driver.find_element_by_xpath('//*[@id="slideBg"]')
picture_url=a.get_attribute('src')


res = requests.get(picture_url,stream=True)  # 获取字节流最好加stream这个参数,原因见requests官方文档
# byte_stream = BytesIO(res.content)  # 把请求到的数据转换为Bytes字节流
# roiImg = Image.open(byte_stream)  # Image打开Byte字节流数据
# #roiImg.show()

image = Image.open(BytesIO(res.content))
image=image.convert("RGB")
arr2 = np.array(image)
for i in range(len(arr2)):
    for j in range(len(arr2[0])):
        if arr2[i][j][0]+arr2[i][j][1]+arr2[i][j][2]>200:
            arr2[i][j][0]=arr2[i][j][1]=arr2[i][j][2]=255
        else:
            arr2[i][j][0]=arr2[i][j][1]=arr2[i][j][2]=0


new_im = Image.fromarray(arr2)
new_im.show()
'''
# iframe = driver.find_element_by_xpath('//iframe')    # 找到“嵌套”的iframe
# driver.switch_to.frame(iframe)     # 切换到iframe

driver.switch_to.default_content()
driver.switch_to.frame("login_frame")
driver.switch_to.frame("tcaptcha_iframe")#我也不懂这个切换模式是什么意思 希望懂的说下

from selenium.webdriver.common.action_chains import ActionChains
def func(i):
    driver.switch_to.default_content()
    driver.switch_to.frame("login_frame")
    driver.switch_to.frame("tcaptcha_iframe")
    button = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')      # 找到“蓝色滑块”
    action = ActionChains(driver)        
    action.reset_actions()
    action.click_and_hold(button)#.perform()
    action.move_by_offset(i, 0).perform()
    action.reset_actions()


# try:
#     func(240)
# except selenium.common.exceptions.MoveTargetOutOfBoundsException:
#     print("GET")

def func1():
    for j in range(200,160,-4):
        try:
            func(j)
            #time.sleep(0.82)#经过测试 每次滑动需要间隔820ms
            time.sleep(0.85)#别问 问就是加了能跑
        except:
            break



func1()

#=================================================================
# all_handles = driver.window_handles   #获取全部页面句柄
# driver.switch_to.window(all_handles[0])  #切换标签页

