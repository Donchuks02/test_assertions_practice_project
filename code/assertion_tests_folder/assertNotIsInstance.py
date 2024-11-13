import unittest

class AssertNotIsInstance(unittest.TestCase):
  def test_case(self):
    def add(x, y):
      return x + y

    self.assertNotIsInstance(add(5, 5), str)


if __name__ == "__main__":
  unittest.main(verbosity=2)