import unittest

class AssertTupleEqual(unittest.TestCase):
  def test_case(self):
    self.assertTupleEqual((1, 2, 3), (1, 2, 3))

  def test_case_fail(self):
    self.assertTupleEqual((1, 2, 3), (1, 2, 4))


if __name__ == '__main__':
  unittest.main(verbosity=2)