# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print("Result:", add(2, 3))

import unittest
import demo1

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demo1.add(2, 3), 5)
        self.assertEqual(demo1.add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
