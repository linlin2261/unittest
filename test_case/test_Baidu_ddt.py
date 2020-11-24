import unittest
import csv
import codecs
from itertools import islice
from selenium import webdriver
from time import sleep
from ddt import ddt,data,file_data,unpack
@ddt
class TestBaidu2(unittest.TestCase):
    """ 百度搜索测试2 """
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bass_url="https://www.baidu.com"
    def baidu_search(self,search_key):
        self.driver.get(self.bass_url)
        sleep(2)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)
    test_data=[["case1","selenium"],["case2","unittest"],["case3","parameterized"]]
    @data(*test_data)
    @unpack
    def test_search1(self,case,search_key):
        print("第一组测试用例:",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    test_data1=(("case1","selenium"),("case2","unittest"),("case3","parameterized"))
    @data(*test_data1)
    @unpack
    def test_search2(self,case,search_key):
        print("第二组测试用例:",case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    test_data2={"search_key":"selenium","search_key":"unittest","search_key":"parameterized"}
    @data({"search_key":"selenium"},{"search_key":"unittest"},{"search_key":"parameterized"})
    @unpack
    def test_search3(self,search_key):
        print("第三组测试用例:",search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    @file_data("D://drivers//unittest//ddt_data_file.json")
    def test_search3(self,search_key):
        print("第四组测试用例:",search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    @file_data("D://drivers//unittest//test_case//ddt_data_file.yaml")
    def test_search4(self,case):
        search_key=case[0]["search_key"]
        print("第五组测试用例:",search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)