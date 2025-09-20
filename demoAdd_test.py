# from demoAdd import add

# def test_add():
#     assert demoAdd.add(2, 3) == 5
#     assert demoAdd.add(0, 0) == 0

import unittest
import demoAdd

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demoAdd.add(2, 3), 5)
        self.assertEqual(demoAdd.add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
