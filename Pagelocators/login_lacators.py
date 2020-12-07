# _*_ coding: utf-8 _*_ 
# time: 2020-11-18  18:07
# name: login_lacators
from selenium.webdriver.common.by import By


class LoginLocator:
    #元素定位
    # 输入用户名
    name = (By.XPATH, "//input[@name='mobile']")
    # 输入密码
    passwd = (By.XPATH, "//input[@name='password']")
    # 点击登录
    login_but = (By.XPATH, "//button[@class='el-button login-btn el-button--primary el-button--medium']")
