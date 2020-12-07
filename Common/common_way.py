# _*_ coding: utf-8 _*_ 
# time: 2020-11-18  15:00
# name: Common_Datas

#封装基本函数-日志，异常，等、、、

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


import logging
import time
import os

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #全局登录地址

    web_url = "http://test.longpean.com/lazada/dist/#/"
    # def web_url(self):
    #     self.driver.get()

    # 等待元素可见
    def  wait_visible(self, locator, time=20, poll_frequency=0.5, mk=""):
        """
        :param locator: 元素定位，元祖形式
        :param time:
        :param poll_frequency:
        :param mk: 模块名，
        :return:
        """
        logging.info("等待{0}可见".format(locator))
        try:
            WebDriverWait(self.driver, time, poll_frequency).until(expected_conditions.visibility_of_element_located(locator))
        except:
            logging.exception("等待元素出现失败")
            #截图
            self.screen_shot(mk)
            raise


    # 等待元素出现
    def wait_appear(self):
        pass

    #查找元素
    def get_element(self, locator, mk = ""):
        logging.info("等待{0}可见".format(locator,mk))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败")
            # 截图
            self.screen_shot(mk)
            raise

    # 点击
    def click_button(self, locator, mk=""):
        clc = self.get_element(locator,mk)
        #元素操作
        logging.info("{0}点击元素：{1}".format(locator,mk))
        #点击操作
        try:
            clc.click()
        except:
            logging.exception("点击失败")
            # 截图
            self.screen_shot(mk)
            raise


    # 输入
    def test_input(self, locator, text, mk=""):
        clc = self.get_element(locator, mk)
        # 输入操作
        logging.info("{0}点击元素：{1}".format(locator, mk))
        try:
            clc.send_keys(text)
        except:
            logging.exception("输入失败")
            # 截图
            self.screen_shot(mk)
            raise

    # 获取文本
    def get_text(self,locator,mk=""):
        clc = self.get_element(locator, mk)
        try:
            return clc.text
        except:
            logging.exception("获取文本失败")
            # 截图
            self.screen_shot(mk)
            raise
    #获取元素属性：
    def get_attribute(self,locator,attr,mk=""):
        clc = self.get_element(locator, mk)
        try:
            return clc.get_attribute(attr)
        except:
            logging.exception("获取元素失败")
            # 截图
            self.screen_shot(mk)
            raise







    #获取id
    #获取name
    #获取class


    #切换iframe表单
    def iframe_switch(self):
        pass

    #强制等待
    def whit_sleep(self):
        pass

    #alert 处理
    def alert_action(self, action="accept"):
        pass
    #截图操作
    def screen_shot(self, name):
        # 生成时间
        creat_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        file_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # 截图路径
        File_Path = os.path.join(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0],"picture") +  "\\" + file_time + "\\"
#os.path.dirname(os.getcwd()) +
        try:
            File_Path = os.path.join(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0],"picture")  + "\\" + file_time + "\\"
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                print("目录新建成功：%s" % File_Path)
            else:
                print("目录已存在！！！")
        except:
            logging.exception("新建目录失败")
        # 图片名称
        file_name = File_Path + creat_time + '.png'.format(name)
        try:
            self.driver.save_screenshot(name)  # 指定截图存放路径和名称
            logging.info("截图成功".format(file_name))
        except:
            logging.exception("截图保存失败")



        self.driver.save_screenshot(file_name)
