import unittest
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.math = Mathematics()

    def test_sum_them(self):
        result = self.math.sum_them(1,2,3,4,5)
        self.assertEqual(result, 15)

    def test_multiply_them(self):
        result = self.math.multiply_them(1,2,3,4,5)
        self.assertEqual(result, 120)

if __name__ == '__main__':
    unittest.main()



