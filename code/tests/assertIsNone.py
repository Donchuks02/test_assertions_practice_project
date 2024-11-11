import unittest

def check(x):
  if x is not int:
    return None


class AssertNone(unittest.TestCase):
  def test_case(self):
    self.assertIsNone(check("num"))


if __name__ == "__main__":
  unittest.main(verbosity=2)