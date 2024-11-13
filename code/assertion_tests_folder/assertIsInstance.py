import unittest

class AssertIsInstance(unittest.TestCase):
  def test_case(self):
    num_classes = (int, float, complex)
    def add(x, y):
      return x + y

    self.assertIsInstance(add(5, 5), num_classes)


if __name__ == "__main__":
  unittest.main(verbosity=2)