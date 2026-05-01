import unittest

from leap_years import is_leap_year

class SmokeTest(unittest.TestCase):
    def test_smoke(self):
        self.assertEqual(1+1, 2)
        self.assertNotEqual(1+1, 3)
        
class LeapYearTests(unittest.TestCase):
    def test_multiples_of_4_are_leap_years(self):
        self.assertEqual(is_leap_year(2024), True)
        self.assertEqual(is_leap_year(2026), False)
    
    def test_multiple_of_100_is_not_leap_year(self):
        self.assertEqual(is_leap_year(1800), False)
    
    def test_multiple_of_400_is_leap_year(self):
        self.assertEqual(is_leap_year(2000), True)
if __name__ == "__main__":
    unittest.main()