import unittest

class AssertIsNotNone(unittest.TestCase):
  def test_case(self):
    name = "Chuks"
    self.assertIsNotNone(name)



if __name__ == "__main__":
  unittest.main(verbosity=2)