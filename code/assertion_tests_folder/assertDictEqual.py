import unittest



class AssertDictEqual(unittest.TestCase):
  def test_case(self):
    self.assertDictEqual({"a": 1, "b": 2}, {"a": 1, "b": 5})


if __name__ == '__main__':
  unittest.main(verbosity=2)