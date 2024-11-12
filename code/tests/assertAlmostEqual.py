import unittest

class AssertAlmostEqual(unittest.TestCase):
  def test_assertAlmostEqual(self):
    self.assertAlmostEqual(10.01, 10.02, places=1)

if __name__ == "__main__":
  unittest.main(verbosity=2)