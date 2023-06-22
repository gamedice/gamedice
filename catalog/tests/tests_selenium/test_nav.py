import time
import unittest
from catalog.tests.tests_selenium import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.settings import URL_FRONT

DELAY = 10
_AMOUNT_NEST_LINKS = 4

class GameCatalog(BaseTest):

    def setUp(self):
        super().setUp()
        self.driver.get(URL_FRONT)

    def test_navigation(self):
        game_link = self._find_by_css_selector( "div[class*=navigation_panel]>div")
        game_link.click()

        navigation_panel_nest = self._find_by_css_selectors("a[class*=nest_link]")

        for nest in range(_AMOUNT_NEST_LINKS):
            game_link.click()
            navigation_panel_nest = self._find_by_css_selectors("a[class*=nest_link]")
            result = navigation_panel_nest[nest].text
            navigation_panel_nest[nest].click()
            WebDriverWait(self.driver, DELAY).until(EC.title_is(result))
            title = self.driver.title
            self.assertEqual(title, result)

        navigation = self._find_by_css_selectors("a[class*=navigation_panel]")

        for element in navigation:
            element.click()
            result = element.text
            title = self.driver.title
            self.assertEqual(title, result)

        image_link = self._find_by_css_selector("a[class*=navigation_image]")
        image_link.click()


if __name__ == "__main__":
    unittest.main()
