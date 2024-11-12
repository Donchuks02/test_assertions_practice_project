import unittest

class AssertMultiLineEqual(unittest.TestCase):

  def test_case(self):
    first_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

    second_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do ut labore et dolore magna aliqua."""

    self.assertMultiLineEqual(first_string, second_string)


if __name__ == "__main__":
  unittest.main(verbosity=2)