import unittest

class AssertIn(unittest.TestCase):
  def test_case(self):
    dept_names = ("Williams", "Patrick", "Mane")
    self.assertIn("Williams", dept_names)

if __name__ == "__main__":
  unittest.main(verbosity=2)