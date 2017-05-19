from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력')

        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('날 수 있도록 공작깃털 사용하기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: 공작깃털 사기')
        self.check_for_row_in_list_table('2: 날 수 있도록 공작깃털 사용하기')

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: 공작깃털 사기', [row.text for row in rows])
        # self.assertIn('2: 날 수 있도록 공작깃털 사용하기', [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
