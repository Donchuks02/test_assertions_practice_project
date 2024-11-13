import unittest

def add():
  x = 5
  y = 5
  return (x + y)


class AssertNotEqual(unittest.TestCase):

  def test_case(self):
    self.assertNotEqual(add(), 11)
    print("\n Yes they are not equal ")


if __name__ == "__main__":
  unittest.main(verbosity=2)