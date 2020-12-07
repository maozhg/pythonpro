# _*_ coding: utf-8 _*_ 
# time: 2020-11-17  16:05
# name: index_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver

class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    def login_out(self):
        #是否存在退出按钮
        try:
            WebDriverWait(self.driver, 20, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
            return True
        except:
            return False