from selenium import webdriver
from time import sleep
from keys import username, password


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(1)


        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(5)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        sleep(4)


if __name__ == '__main__':
    InstaBot()