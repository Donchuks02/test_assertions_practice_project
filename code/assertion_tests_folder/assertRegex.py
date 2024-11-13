import unittest

class AssertRegex(unittest.TestCase):
    def test_case(self):
        text = "The quick brown fox jumps over the lazy dog using this email john.doe@gmail.com"
        self.assertRegex(text, r"@gmail\.com")


if __name__ == "__main__":
  unittest.main(verbosity=2)