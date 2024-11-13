import unittest

class AssertSetEqual(unittest.TestCase):

  def test_case(self):
    a = {1, 2, 3}
    b = {1, 2, 3}
    self.assertSetEqual(a, b)

if __name__ == "__main__":
  unittest.main(verbosity=2)