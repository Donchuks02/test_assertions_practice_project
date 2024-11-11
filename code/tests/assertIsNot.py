import unittest

first_name = 'chuks_chuks'
last_name = 'chuks'

class AssertIs(unittest.TestCase):

  def test_case(self):
    self.assertIsNot(first_name, last_name)


if __name__ == '__main__':
  unittest.main(verbosity=2)