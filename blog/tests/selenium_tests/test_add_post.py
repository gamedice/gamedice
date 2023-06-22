import os
import time
import random

import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conf.settings import URL_FRONT
from blog.tests.selenium_tests import BaseTest


class AddPostToBlogTestCase(BaseTest):

    def setUp(self):
        super().setUp()
        self.driver.get(f"{URL_FRONT}/blog/new_post")

    def test_add_post(self):

        text_to_post_title_check = str(random.randint(1, 1000))
        text_to_post_contain_check = str(random.randint(1, 1000))
        id_user_to_post_check = "1"

        absolute_path = os.path.dirname(__file__)
        relative_path = "img/harry.jpg"
        full_path_to_photo = os.path.join(absolute_path, relative_path)

        photo_to_post = self._find_by_css_selector("input[class*=photo_to_post]")
        photo_to_post.send_keys(full_path_to_photo)

        checkbox_is_published = self._find_by_css_selector("input[class*=is_published]")
        checkbox_is_published.click()

        text_to_post_title = self._find_by_css_selector("textarea[class*=text_to_post_title]")
        text_to_post_title.click()
        text_to_post_title.send_keys(text_to_post_title_check)

        text_to_post_contain = self._find_by_css_selector("textarea[class*=text_to_post_contain]")
        text_to_post_contain.click()
        text_to_post_contain.send_keys(text_to_post_contain_check)

        id_user_to_post = self._find_by_css_selector("input[class*=id_user_to_post]")
        id_user_to_post.click()
        id_user_to_post.send_keys(id_user_to_post_check)

        btn_add_post = self._find_by_css_selector("button[class*=btn_add_post]")
        btn_add_post.click()

        link_after_add_post = self._find_by_css_selector("a[class*=link_after_add_post]")
        link_after_add_post_is_displayed = link_after_add_post.is_displayed()

        self.assertTrue(link_after_add_post_is_displayed)

        link_after_add_post.click()
        try:
            if link_after_add_post.is_displayed():
                link_after_add_post.click()
        except:
            print('\nCorrect\n')
            pass

        post_title_in_blog = self._find_by_css_selector("h5[class*=post_title_in_blog]").text
        self.assertEquals(text_to_post_title_check, post_title_in_blog)

        post_contain_in_blog = self._find_by_css_selector("p[class*=post_contain_in_blog]").text
        self.assertEquals(text_to_post_contain_check, post_contain_in_blog)

    def test_empty_title(self):
        btn_add_post = self._find_by_css_selector("button[class*=btn_add_post]")
        btn_add_post.click()

        wrn_empty_title = self._find_by_css_selector("p[class*=text-red-500]").is_displayed()
        self.assertTrue(wrn_empty_title)

    def test_empty_contain(self):
        text_to_post_title_check = "post's title from selenium"

        text_to_post_title = self._find_by_css_selector("textarea[class*=text_to_post_title]")
        text_to_post_title.send_keys(text_to_post_title_check)

        self._find_by_css_selector("button[class*=btn_add_post]").click()

        wrn_empty_contain = self._find_by_css_selector("p[class*=text-red-500]").is_displayed()
        self.assertTrue(wrn_empty_contain)
