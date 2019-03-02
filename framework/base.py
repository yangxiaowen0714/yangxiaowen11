from  selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from framework.logger import Logger
import os
from selenium import webdriver
logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):  #浏览器后退按钮
        self.driver.back()
        logger.info("Click back on current page.")
    def forward(self):  #浏览器前进按钮
        self.driver.forward()
        logger.info("Click forward on current page.")
    def open_url(self,url):  #打开连接
        self.driver.get(url)
    def quit_browser(self):#关闭并停止浏览器服务
        self.driver.quit()
    def close(self):  #关闭链接
        try:
            self.driver.close()
            logger.info("Closing and quit the brower.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s"%e)
            self.get_windows_img()
    def find_element(self,*loc): #查找页面元素
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素-->%s" %loc)

        except:
            logger.error("%s页面中未能找到%s元素"%(self,loc))
            self.get_windows_img()
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+'/screenshots/'
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder:/screenshots")
        except Exception as e:
            logger.error("Failed to take screenshot!%s"%e )
            self.get_windows_img()
    def sendkeys(self,text,*loc):  #输入
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容:%s"%text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" %e)
            self.get_windows_img()
    def clear(self,*loc):  #清除文本框
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("Clear text in input box before typing")
        except Exception as e:
            logger.error("Failed to clear in input box with %s"%e)
            self.get_windows_img()
    def click(self,*loc): #点击元素
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("The element %s was clicked."%(el.text))
        except Exception as e:
            logger.error("Failed to click the element with %s"%e)
            self.get_windows_img()
    def switch_to_frame(self,n):
        iframe = self.driver.find_elements_by_tag_name("iframe")[n]
        self.driver.switch_to.frame(iframe)
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def gettext(self,*loc):
        el=self.find_element(*loc)
        try:
            return el.text
        except Exception as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()
