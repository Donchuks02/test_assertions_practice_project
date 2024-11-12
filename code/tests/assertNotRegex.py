import unittest

class AssertNotRegex(unittest.TestCase):
    def test_case(self):
        text = "The quick brown fox jumps over the lazy dog "
        self.assertNotRegex(text, r"brown")


if __name__ == "__main__":
  unittest.main(verbosity=2)