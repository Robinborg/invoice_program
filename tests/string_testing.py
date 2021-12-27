import unittest


class TestStringInput(unittest.TestCase):
    def test_numerical_input(self):
        self.assertEqual("1", "FOO")

if __name__ == "__main__":
    unittest.main()


