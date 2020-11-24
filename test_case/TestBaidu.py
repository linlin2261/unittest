import unittest
from selenium import webdriver
from time import sleep
class TestBaidu(unittest.TestCase):
    """ 百度搜索测试 """
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bass_url="https://www.baidu.com"
    def baidu_search(self,search_key):
        self.driver.get(self.bass_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)
    def test_search_key_selenium(self):
        """ 搜索关键字:senlenium """
        search_key="selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    def test_search_key_unttest(self):
        """ 搜索关键字:unittest """
        search_key="unittest"
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=='__main__':
    unittest.main()