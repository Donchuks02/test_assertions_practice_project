import unittest
from tests.assertGreater import mul, add

class AssertLessEqual(unittest.TestCase):
  def test_case(self):
    self.assertLessEqual(mul() , add() )


if __name__ == "__main__":
  unittest.main(verbosity=2)