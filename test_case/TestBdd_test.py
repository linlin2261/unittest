import unittest
class TestBdd(unittest.TestCase):
    def setUp(self):
        print("test TestBdd:")
    def test_ccc(self):
        print("test ccc")
    def test_aaa(self):
        print("test aaa")
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test TestAdd")
    def test_bbb(self):
        print("test bbb")
if __name__=='__main__':
    #unittest.main()
    suit=unittest.TestSuite()
    suit.addTest(TestBdd("test_aaa"))
    suit.addTest(TestAdd("test_bbb"))
    suit.addTest(TestBdd("test_ccc"))
  
    
    runner = unittest.TextTestRunner(stream=None, descriptions=None, verbosity=0)

    runner.run(suit)
            