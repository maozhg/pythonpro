# _*_ coding: utf-8 _*_ 
# time: 2020-11-18  13:41
# name: login

import unittest
import logging
from time import sleep
from selenium import webdriver
from Pageobjects.login_page import LoginPage
from Pageobjects.index_page import IndexPage
from Common.common_way import BasePage
from Testdates.login import login_data
# import ddt

# @ddt.ddt

class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        print(1)
        cls.driverfile_path = r'E:\driver\chromedriver.exe'  # 驱动路径
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # 浏览器最大化
        sleep(2)
        cls.driver.get(BasePage.web_url) # 打开
        cls.lg = LoginPage(cls.driver)

        sleep(5)


    @classmethod
    def tearDownClass(cls):
        sleep(10)
        cls.driver.quit()


    def tearDown(self) -> None:
        # 刷新页面
        self.driver.refresh()

#    #正常登录
    def test_login_1(self):
        logging.info("登录")
        self.lg.login(login_data.success_data["phone"], login_data.success_data["password"])
        #断言
        self.assertTrue(IndexPage(self.driver).login_out())

    #异常情况1,ddt
    # @ddt.data(*login.phone_data)
    # def test_login_2(self,data):
    #     self.lg.login(data["phone"], data["password"])
    #     断言
    #     self.assertEqual(self.lg.login_ts1(),data["check"])
    #异常情况，弹窗提示
    # def test_login_3(self):







