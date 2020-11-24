import unittest
from leap_year import LeapYear
class TestLeapYear(unittest.TestCase):
    def setUp(self):
        print("test start")
    def tearDown(self):
        print("test end")
    def test_2000(self):
        ly=LeapYear(2000)
        self.assertEqual(ly.answer(),"2000是闰年")
    def test_2004(self):
        ly=LeapYear(2004)
        self.assertEqual(ly.answer(),"2004是闰年")
    def test_20041(self):
        ly=LeapYear(2004)
        self.assertEqual(ly.answer(),"2004不是闰年")
    def test_2017(self):
        ly=LeapYear(2017)
        self.assertEqual(ly.answer(),"2017不是闰年")
    def test_2100(self):
        ly=LeapYear(2100)
        self.assertEqual(ly.answer(),"2100不是闰年")
if __name__=='__main__':
    suit=unittest.TestSuite()
    suit.addTest(TestLeapYear("test_2000"))
    suit.addTest(TestLeapYear("test_20041"))
    runner=unittest.TextTestRunner()
    runner.run(suit)