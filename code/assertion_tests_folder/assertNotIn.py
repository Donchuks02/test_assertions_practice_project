import unittest

class AssertNotIn(unittest.TestCase):
  def test_case(self):
    dept_names = ("Williams", "Patrick", "Mane")
    self.assertNotIn("Williams", dept_names)

if __name__ == "__main__":
  unittest.main(verbosity=2)