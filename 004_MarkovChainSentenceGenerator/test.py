import unittest
import markover

class TestCode(unittest.TestCase):

  def test_genPairs(self):
    self.assertEqual(markover.genPairs(["Hmm", ".", ".", "."]), {'.':[], ",":[], "Hmm":['.']})
    self.assertEqual(markover.genPairs(['cat', 'bit', 'a', 'ham', '.', 'dog', 'bit', 'a', 'cat', '.']), {'ham': ['.'], 'dog': ['bit'], 'cat': ['bit', '.'], 'a': ['ham', 'cat'], '.': [], ',': [], 'bit': ['a', 'a']})

  def test_prepareSentence(self):
    self.assertEqual(markover.prepareSentence("Cat bit a ham. Dog bit a cat."), ['cat', 'bit', 'a', 'ham', '.', 'dog', 'bit', 'a', 'cat', '.'])
    self.assertEqual(markover.prepareSentence("Hm..."), ["hm", ".", ".", "."])
    self.assertEqual(markover.prepareSentence("Hm.,."), ["hm", ".", ",", "."])
    pass

  def test_getSentence(self):
    pass

  #def generateChain(self):
  # pass

if __name__ == "__main__":
  unittest.main()
