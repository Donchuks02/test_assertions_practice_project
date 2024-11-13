import unittest

def add():
  a = 10
  b = 10
  return (a + b)


def mul():
  a = 10
  b = 10
  return (a * b)


class AssertGreater(unittest.TestCase):
  def test_case(self):
    self.assertGreater(mul() , add() )



if __name__ == "__main__":
  unittest.main(verbosity=2)