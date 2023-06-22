import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        firefoxOptions = Options()
        firefoxOptions.headless = True

        firefox = Service('geckodriver')
        self.driver = webdriver.Firefox(service=firefox, options=firefoxOptions)

        self.driver.maximize_window()

    def _find_by_css_selector(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def _find_by_css_selectors(self, selector):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def tearDown(self):
        self.driver.close()
