import unittest

class SmokeTest(unittest.TestCase):
    def test_smoke(self):
        self.assertEqual(1+1, 2)
        self.assertNotEqual(1+1, 3)
        
if __name__ == "__main__":
    unittest.main()