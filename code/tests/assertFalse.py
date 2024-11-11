import unittest


class AssertFalse(unittest.TestCase):
  def test_case(self):
    my_age = 20
    self.assertFalse(isinstance(my_age, str))


if __name__ == '__main__':
  unittest.main(verbosity=2)