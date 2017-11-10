import unittest

class TestClass08(unittest.TestCase):
    """docstring for TestClass08."""
    def test_case01(self):
        self.assertTrue("PYTHON".isupper(), 'message')
        print("\nIn test_case01()")

    def test_case02(self):
        self.assertFalse("Python".isupper(), 'message')
        print("\nIn test_case01()")

    def test_case03(self):
        self.assertTrue(True, 'message')
        print("\nIn test_case03()")
