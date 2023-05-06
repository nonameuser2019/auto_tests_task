
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser: webdriver.Chrome, timeout=10):
        self.browser = browser
        self.url = None
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

