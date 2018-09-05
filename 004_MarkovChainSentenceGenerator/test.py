import unittest
import markover

class TestCode(unittest.TestCase):

  def test_genPairs(self):
    pass

  def test_prepareSentence(self):
    self.assertEqual(markover.prepareSentence("Cat bit a ham. Dog bit a cat."), ['cat', 'bit', 'a', 'ham', '.', 'dog', 'bit', 'a', 'cat', '.'])
    pass

  def test_getSentence(self):
    pass

  #def generateChain(self):
  # pass

if __name__ == "__main__":
  unittest.main()
