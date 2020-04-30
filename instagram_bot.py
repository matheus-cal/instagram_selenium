from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(2)


if __name__ == '__main__':
    InstaBot()
