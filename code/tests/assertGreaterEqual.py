import unittest
from tests.assertGreater import mul, add

class AssertGreaterEqual(unittest.TestCase):
  def test_case(self):
    self.assertGreaterEqual(mul() , add() )




if __name__ == "__main__":
  unittest.main(verbosity=2)