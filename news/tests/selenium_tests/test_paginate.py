import time
from blog.tests.selenium_tests import BaseTest
from conf.settings import URL_FRONT

_MAX_RETRIES = 3


class ClickNewsTestCase(BaseTest):

    def setUp(self):
        super().setUp()
        self.driver.get(f"{URL_FRONT}/news")

    def assert_retry_equals(self, expected_num, num_to_check, arrow):
        for i in range(_MAX_RETRIES):
            try:
                self.assertEquals(expected_num, num_to_check)
            except AssertionError:
                time.sleep(1)
                arrow.click()
                current_page = self._find_by_css_selector("p[class*=current_page]")
                num_to_check = current_page.get_attribute("textContent")
                self.assertEquals(expected_num, num_to_check)

    def test_click_paginate(self):
        num_second_page_check = 'page 2'
        arrow_next = self._find_by_css_selector("span[class*=next]")
        arrow_next.click()

        current_page_hidden = self._find_by_css_selector("p[class*=current_page]")
        num_second_page = current_page_hidden.get_attribute("textContent")

        # assertRetryEquals = lambda num_check=num_second_page_check, num_page=num_second_page, arrow=arrow_next: \
        #     self.assert_retry_equals(num_check, num_page, arrow)
        # assertRetryEquals()

        self.assert_retry_equals(num_second_page_check, num_second_page, arrow_next)

        num_first_page_check = 'page 1'
        arrow_prev = self._find_by_css_selector("span[class*=prev]")
        arrow_prev.click()

        current_page_hidden = self._find_by_css_selector("p[class*=current_page]")
        num_first_page = current_page_hidden.get_attribute("textContent")

        self.assert_retry_equals(num_first_page_check, num_first_page, arrow_prev)
