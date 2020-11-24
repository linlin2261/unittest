import unittest
import csv
import codecs
from itertools import islice
from selenium import webdriver
from time import sleep
from parameterized import parameterized
class TestBaidu2(unittest.TestCase):
    """ 百度搜索测试2 """
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bass_url="https://www.baidu.com"
    def baidu_search(self,search_key):
        self.driver.get(self.bass_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)
    @parameterized.expand([
        ("case1","selenium"),
        ("case2","unittest"),
        ("case3","parameterized"),
    ])
    def test_search(self,name,search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)