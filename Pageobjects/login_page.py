from selenium import webdriver
from Pagelocators.login_lacators import LoginLocator
from Common.common_way import BasePage



class LoginPage(BasePage):




    #登录
    def login(self, username: object, password: object) -> object:


        mk = "登录"
        #等待元素出现
        self.wait_visible(LoginLocator.login_but, mk=mk)
        self.test_input(LoginLocator.name, username, mk)
        self.test_input(LoginLocator.passwd, password, mk)
        self.click_button(LoginLocator.login_but, mk)

    # 获取登录错误提示，登录区域
    # def login_ts1(self):
    #     WebDriverWait(self.driver, 30, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
    #     return self.driver.find_element_by_xpath("//*[text()='平台']")
    #获取登录错误提示，弹窗
    # def login_ts2(self):
    #     WebDriverWait(self.driver, 30, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
    #     return self.driver.find_element_by_xpath("//*[text()='平台']")
