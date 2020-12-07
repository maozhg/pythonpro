
from _multiprocessing import send
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains



if __name__ == '__main__':
    driverfile_path = r'E:\driver\chromedriver.exe'  # 驱动路径
    driver = webdriver.Chrome(service_log_path="E://LOG.log")  # 启动浏览器
    driver.get('http://test.longpean.com/lazada//#/')  # 打开longpean
    driver.maximize_window()  # 浏览器最大化
    a = driver.find_element_by_xpath("//input[@name='mobile']").send_keys("15026603384")  # 帐号

    driver.find_element_by_xpath("//input[@name='password']").send_keys("123123")  # 密码
    driver.find_element_by_xpath("//button[@class='el-button login-btn el-button--primary el-button--medium']").click()
    # WebDriverWait(driver, 30, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
    WebDriverWait(driver, 30, 0.2).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='平台']")))
    sleep(5)
    # move = driver.find_elements_by_xpath( "//*[text()='平台']").click()
    # ActionChains(driver).move_to_element(move).perform()
    # WebDriverWait(driver, 30, 0.2).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='router-link-exact-active router-link-active']"))
    # driver.find_element_by_xpath( "//a[@class='router-link-exact-active router-link-active']").click()

    driver.close()

    move = driver.find_elements_by_xpath( "//*[text()='平台']").click()