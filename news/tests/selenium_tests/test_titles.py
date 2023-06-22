import time

from blog.tests.selenium_tests import BaseTest
from conf.settings import URL_FRONT


class CheckTitleNewsTestCase(BaseTest):

    def setUp(self):
        super().setUp()
        self.driver.get(f"{URL_FRONT}/news")

    def test_check_titles(self):

        all_news_amount = len(self._find_by_css_selectors("div[class*=one_card]"))

        for i in range(all_news_amount):
            try:
                news_title_all = self._find_by_css_selectors("h5[class*=title_card_news]")
                title_news = news_title_all[i].text
            except IndexError:
                print("===== IndexError =====")
                time.sleep(1)
                news_title_all = self._find_by_css_selectors("h5[class*=title_card_news]")
                title_news = news_title_all[i].text

            all_news_link = self._find_by_css_selectors("a[class*=button_to_news_item]")
            all_news_link[i].click()
            news_title = self._find_by_css_selector("h5[class*=title_item]").text
            self.driver.back()
            self.assertEquals(title_news, news_title)

