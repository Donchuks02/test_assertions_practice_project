import unittest


class AssertSequenceEqual(unittest.TestCase):
  def test_case(self):
    self.assertSequenceEqual([1, 2, 3], [1, 2, 3])


if __name__ == "__main__":
  unittest.main(verbosity=2)