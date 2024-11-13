import unittest

def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

class AssertIs(unittest.TestCase):

  def test_case(self):
    self.assertIs(add(5, 5), sub(5, 5))


if __name__ == '__main__':
  unittest.main(verbosity=2)