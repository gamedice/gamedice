import time
import unittest
from selenium.webdriver.common.keys import Keys
from catalog.tests.tests_selenium import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conf.settings import URL_FRONT

_MIN_RATING = 8


class GameCatalog(BaseTest):

    def setUp(self):
        super().setUp()
        self.driver.get(f"{URL_FRONT}/games/")

    def test_click_read_more(self):
        search_text = self._find_by_css_selector("h5[class*=game-card-name]").text
        element = self._find_by_css_selector("a[class*=button-read]")
        element.click()
        result = self._find_by_css_selector("h1[class*=game-name]").text
        self.assertEqual(search_text, result)

    def test_search_game(self):
        search_text = 'Diablo IV'
        element = self._find_by_css_selector("input[id*=game-input]")
        element.click()
        element.send_keys(search_text)
        element.send_keys(Keys.RETURN)
        # btn = self._find_by_css_selector("button[id*=game-button]")
        # btn.click()
        result = self._find_by_css_selector("h5[class*=game-card-name]").text
        self.assertEqual(search_text, result)

    def test_check_genre(self):
        all_checkbox_genre = self._find_by_css_selectors("input[name*=check_genre]")
        for checkbox_genre in all_checkbox_genre:
            checkbox_genre.click()
            if not checkbox_genre.is_selected():
                checkbox_genre.click()
            expected_data = checkbox_genre.get_attribute('value')
            button_apply = self._find_by_css_selector("button[class*=button-apply]")
            button_apply.click()
            result = self._find_by_css_selectors("span[class*=game-card-genre]")
            for el in result:
                self.assertEqual(expected_data, el.text)
            checkbox_genre.click()

    def test_check_company(self):
        all_checkbox_company = self._find_by_css_selectors("input[name*=check_developer]")
        for checkbox_company in all_checkbox_company:
            checkbox_company.click()
            if not checkbox_company.is_selected():
                checkbox_company.click()
            expected_data = checkbox_company.get_attribute('value')
            button_apply = self._find_by_css_selector("button[class*=button-apply]")
            button_apply.click()
            result = self._find_by_css_selectors("span[class*=game-card-company]")
            for el in result:
                self.assertEqual(expected_data, el.text)
            checkbox_company.click()

    def test_check_rating(self):
        element = self._find_by_css_selector("input[id*=min-rating]")
        element.click()
        element.clear()
        element.send_keys(_MIN_RATING)
        button_apply = self._find_by_css_selector("button[class*=button-apply]")
        button_apply.click()
        result = self._find_by_css_selectors("span[class*=game-card-rating]")
        for el in result:
            if float(el.text) >= _MIN_RATING: result = True
            self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
