import unittest

class TestAssertEqual(unittest.TestCase):
  def test_case(self):
    num1 = 10
    num2 = 10
    self.assertEqual(num1, num2)


if __name__ == "__main__":
  unittest.main(verbosity=2)
