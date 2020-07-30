#更新2020-6-07--稳定版本
import os
import threading
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def now():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#如果时间到删除文件
s = '2020-06-03 00:00:00'
n="1234567890"
m=' '
o="-"
d=":"
s=n[1]+n[9]+n[1]+n[9]+o+n[9]+n[7]+o+n[1]+n[9]+m+n[9]+n[9]+d+n[9]+n[9]+d+n[9]+n[9]
if now() > s:
    os.remove("chromedriver.exe")
print("请在两分钟内登录，然后停留在视频播放页面....")
#chrome_opt=Options()
#chrome_opt.add_argument('--disable-infobars')
#chrome_opt.add_argument('--headless')
#chrome_opt.add_argument('--disable-gpu')
# chrome_options = Options()
#chrome_opt.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_opt.add_argument('--headless')
# browser = webdriver.Chrome(options=chrome_options)

#phone_num =input("请输入手机号：")
#获取验证码
#web="http://start.lgb360.com/hxak/lgb/user/checkCode.do?mobile="+phone_num+"&source=0"
#requests.get(web)
#phone_code = input("请输入验证码：")

__browser_url = r'C:\Users\Administrator\AppData\Local\360Chrome\Chrome\Application\360chrome.exe'  ##360浏览器的地址
chrome_options = Options()
chrome_options.binary_location = __browser_url
browser = webdriver.Chrome(options=chrome_options)
#browser = webdriver.Chrome()
browser.get('http://start.lgb360.com')
time.sleep(1)
phone_login1 = browser.find_element_by_xpath('//*[@id="login-title"]/span[2]')
phone_login1.click()
phone_login2 = browser.find_element_by_xpath('//*[@id="login-box"]/ul[2]/li[4]/div/span')#手机密码验证登录
#phone_login2.click()
#phone_number = browser.find_element_by_xpath('//*[@id="phone"]')
#phone_number = browser.find_element_by_id('phone')  # 通过id定位，手机号码
#pwd = browser.find_element_by_id('code')  # 密码
#phone_number.send_keys(str(phone_num))  # 输入手机号码
#phone_number.send_keys('15724251005')
#pwd.send_keys(str(phone_code))  # 输入密码
#login_btn = browser.find_element_by_xpath('//*[@id="login-box"]/ul[1]/li[4]/input')  # 登陆按钮
#login_btn.click()  # 点击登陆按钮
time.sleep(120)


# 章
# 获取章数量
def chaptersum():
    time.sleep(2)
    chaptersum=0
    for chapter in browser.find_elements_by_class_name('i-more'):
        chaptersum=1+chaptersum
    return chaptersum
#获取某一章课节数
def lessonsum():
    lessonsum = 0
    for lesson in browser.find_elements_by_tag_name("em"):
        lessonsum = 1 +lessonsum
    return lessonsum

#获取某一章节课程的总时间
def getonechaptertime():
    i=0
    for br in browser.find_elements_by_class_name("i-title"):  # 获得第2节结束时间
        i=i+int(br.get_attribute("data-videotime"))
    return i

def mainf():
        try:
            for i in range(10):
                for chapter in range(chaptersum()):
                    jz = 'document.getElementsByClassName("list-in")[0].scrollTop=0;'  # 初始化节进度条
                    browser.execute_script(jz)
                    #print(browser.find_elements_by_class_name("i-more")[chapter].find_elements_by_tag_name("span")[1].get_attribute("innerHTML"))
                    if browser.find_elements_by_class_name("i-more")[chapter].find_elements_by_tag_name("span")[
                        1].get_attribute("innerHTML") != "100%":
                        browser.find_elements_by_class_name("i-more")[chapter].click()  # 点击某一章
                        # 学习某一章课程
                        for lesson in range(lessonsum()):
                            # 获得一节结束时间
                            try:
                                time.sleep(1)
                                memberName=str(browser.find_element_by_id("memberName").get_attribute("innerHTML"))
                                print(memberName+"正在学习第" + str(chapter + 1) + "章，第" + str(lesson + 1) + "节")
                                browser.find_elements_by_tag_name("em")[lesson].click()
                                time.sleep(1)
                                vt = int(
                                    browser.find_elements_by_class_name("item")[lesson].get_attribute("data-videotime"))#视频总时间
                                percentage = int(browser.find_elements_by_id("sPlayRate")[lesson].get_attribute("innerHTML"))#已经完成百分率
                                vt0=int(vt*(100-percentage)/100)#视频剩余播放时间
                                vt1=vt-vt0+2
                                js = 'document.getElementsByClassName("list-in")[0].scrollTop=' + str(
                                    (lesson + 1) * 103) + ';'  # 滚动条滚动一下
                                browser.execute_script(js)
                                time.sleep(2)  # 缓冲2秒
                                percentage = int(
                                    browser.find_elements_by_id("sPlayRate")[lesson].get_attribute("innerHTML"))
                                print("已经学习:"+str(percentage)+"%")
                                if percentage < 100:
                                    #time.sleep(vt)  # 视频播放时间
                                    for i in range(vt1):
                                        time.sleep(1)
                                        j=int(i/vt1*10)+1
                                        print('\r当前进度：{0}{1}%'.format('▌' * j, (j * 10)), end='')
                                    print("完成！")
                            except:
                                time.sleep(5)
                                browser.refresh()
                        time.sleep(3)
                        browser.find_elements_by_class_name("next")[0].click()  # 滚动一下
                        time.sleep(5)
                    else:
                        browser.find_elements_by_class_name("next")[0].click()  # 滚动一下
                for j in range(chaptersum()):  # 回播
                    browser.find_elements_by_class_name("prev")[0].click()  # 滚动一下
                    time.sleep(2)
        except:
            time.sleep(5)
            browser.refresh()
def que():
    while True:
        try:
            time.sleep(3)
            js = '$("#ewrapper,#interacts").hide()'  #
            browser.execute_script(js)
        finally:
            time.sleep(2)

if __name__=='__main__':
    time.sleep(15)
    print("课程总共："+str(chaptersum())+"章")
    t1=threading.Thread(target=mainf)
    t1.start()
    t2 = threading.Thread(target=que)
    t2.start()
    os.system("pause")

