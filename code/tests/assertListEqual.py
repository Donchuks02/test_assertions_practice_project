import unittest

class AssertListEqualTest(unittest.TestCase):

  def test_case(self):
    self.assertListEqual([1, 2, 3], [1, 2, 3])

  def test_case_fail(self):
    self.assertListEqual([1, 2, 3], [1, 2, 3, 4])

if __name__ == "__main__":
  unittest.main(verbosity=2)