import unittest
from tests.assertGreater import mul, add

class AssertLess(unittest.TestCase):
  def test_case(self):
    self.assertLess(mul() , add() )


if __name__ == "__main__":
  unittest.main(verbosity=2)