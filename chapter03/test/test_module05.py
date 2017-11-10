import unittest

def setUpModule():
    """Called once, before anything else in this module"""
    print("In setUpModule()...")

def tearDownModule():
    """Called once, after anything else in this module"""
    print("In tearDownModule()...")

class TestClass06(unittest.TestCase):
    """docstring for TestClass06."""
    @classmethod
    def setUpClass(cls):
        """called once, before any test"""
        print("in setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """called once, after alltest test if setUpClass succesful"""
        print("in tearDownClass()...")

    def setUp(self):
        """called multiple times, before every test method"""
        print("\nin setUp()...")

    def tearDown(self):
        """called multiple times, after every test method"""
        print("\nin tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("in test_case01()")

    def test_case02(self):
        self.assertFalse("python".isupper())
        print("in test_case02()")

# if __name__ == '__main__':
#     unittest.main()
