import unittest

class AssertTrue(unittest.TestCase):
  def test_case(self):
    my_str = "CHUKS"
    self.assertTrue(my_str.isupper())

if __name__ == "__main__":
  unittest.main(verbosity= 2)