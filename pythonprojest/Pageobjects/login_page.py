from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Pagelocators.login_lacators import LoginLocator


class LoginPage:


    def __init__(self,driver):

        self.driver = driver

    #登录
    def login(self, username: object, password: object) -> object:

        #输入用户名
        #输入密码
        #点击登录
        # name = "//input[@name='mobile']"
        # passwd = "//input[@name='password']"
        # login_but = "//button[@class='el-button login-btn el-button--primary el-button--medium']"
        WebDriverWait(self.driver, 20, 0.2).until(expected_conditions.visibility_of_element_located((LoginLocator.login_but)))
        self.driver.find_element(*LoginLocator.name).send_keys(username)
        self.driver.find_element(*LoginLocator.passwd).send_keys(password)
        self.driver.find_element(*LoginLocator.login_but).click()
        # 获取登录错误提示，登录区域
    # def login_ts1(self):
    #     WebDriverWait(self.driver, 30, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
    #     return self.driver.find_element_by_xpath("//*[text()='平台']")
    #     获取登录错误提示，弹窗
    #     WebDriverWait(self.driver, 30, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
    #      return self.driver.find_element_by_xpath("//*[text()='平台']")
