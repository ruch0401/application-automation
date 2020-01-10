from selenium import webdriver
from time import sleep

class LogIn:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://you.usc.edu/login/")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"login_username\"]").send_keys("ruch0401@gmail.com")
        self.driver.find_element_by_xpath("//input[@name=\"login_password\"]").send_keys("****")
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()
        self.driver.find_element_by_xpath("//input[@name=\"login_submit\"]").click()

LogIn()