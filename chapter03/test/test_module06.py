import unittest

class TestClass07(unittest.TestCase):
    """docstring for TestClass07."""
    def test_case01(self):
        self.assertTrue("PYTHON".isupper(), 'message')
        print("\nIn test_case01()")
