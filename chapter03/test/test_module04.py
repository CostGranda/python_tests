import unittest
import inspect

class TestClass04(unittest.TestCase):
    """docstring for TestClass04."""
    def test_case01(self):
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test method : " + inspect.stack()[0][3])

class TestClass05(unittest.TestCase):
    """docstring for TestClass04."""
    def test_case01(self):
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test method : " + inspect.stack()[0][3])

if __name__ == '__main__':
    unittest.main(verbosity=2)
