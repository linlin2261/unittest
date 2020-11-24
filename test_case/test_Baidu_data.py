import unittest
import csv
import codecs
from itertools import islice
from selenium import webdriver
from time import sleep
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
    def test_search(self):
        with codecs.open("D://drivers//unittest//baidu_data.csv",'r','utf-8')as f:
            print("kaishi")
            data=csv.reader(f)
            for line in islice(data,1,None):
                search_key=line[1]
                print(search_key)
                self.baidu_search(search_key)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)