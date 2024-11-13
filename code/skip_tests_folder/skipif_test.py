import unittest




class SkipIfTest(unittest.TestCase):
  def names_dict():
    names = {
        "name1": "Paul",
        "name2": "James",
        "name3": "Patrick"
    }
    return names


  @unittest.skipIf(names_dict().__class__ == dict , "Skipped because names_dictionary is a dictionary")
  def test_case(self):
    pass



if __name__ == "__main__":
  unittest.main(verbosity=2)