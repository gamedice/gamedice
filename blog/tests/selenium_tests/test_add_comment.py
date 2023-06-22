from blog.tests.selenium_tests import BaseTest
from conf.settings import URL_FRONT


class AddCommentToPostTestCase(BaseTest):

    def setUp(self):
        super().setUp()
        self.driver.get(f"{URL_FRONT}/blog")

        btn_to_post = self._find_by_css_selector("a[class*=button_to_blog_item]")
        btn_to_post.click()

    def test_add_comment(self):
        text_check = "comment from selenium"
        id_user_to_comment_check = "1"

        comment_field = self._find_by_css_selector("textarea[class*=comment_field]")
        comment_field.send_keys(text_check)

        id_user_to_comment = self._find_by_css_selector("input[class*=id_user_to_comment]")
        id_user_to_comment.send_keys(id_user_to_comment_check)

        btn_add_comment = self._find_by_css_selector("button[class*=btn_add_comment]")
        btn_add_comment.click()

        self.driver.refresh()

        comm_to_post = self._find_by_css_selector("div[class*=comm_to_post]").text

        self.assertEquals(text_check, comm_to_post)

    def test_add_empty_comment(self):
        btn_add_comment = self._find_by_css_selector("button[class*=btn_add_comment]")
        btn_add_comment.click()

        wrn_empty_comment = self._find_by_css_selector("p[class*=text-red-500]").is_displayed()

        self.assertTrue(wrn_empty_comment)
