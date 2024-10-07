import unittest
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_second(self):
        self.assertEqual(10, 10)


if __name__ == '__main__':
    unittest.main()
