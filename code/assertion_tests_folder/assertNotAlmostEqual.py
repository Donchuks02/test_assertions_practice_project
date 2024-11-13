import unittest

class AssertNotAlmostEqual(unittest.TestCase):
    def test_case(self):
        self.assertNotAlmostEqual(10.01, 10.02, places=2)



if __name__ == "__main__":
  unittest.main(verbosity=2)