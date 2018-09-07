import unittest
import RPNer as rer

class TestCode(unittest.TestCase):
    def test_tokenize(self):
      self.assertEqual(rer.tokenize("4 8 9 + +"), ['4', '8', '9', '+', '+'])
      self.assertEqual(rer.tokenize("48 9 + +"), ['48', '9', '+', '+'])
      self.assertEqual(rer.tokenize("48 s"), ['48'])
      self.assertEqual(rer.tokenize("sa q"), ['q'])
    def test_parse(self):
      self.assertEqual(rer.parse(['48']), [48])
      self.assertEqual(rer.parse(['+']), ['+'])
      self.assertEqual(rer.parse(['+', '48']), ['+', 48])
      self.assertEqual(rer.parse([]), [])
    def test_evaluate(self):
      self.assertEqual(rer.evaluate([4, 5, '+'], []), [9])
      self.assertEqual(rer.evaluate(['+'], [4, 5]), [9])

if __name__ == "__main__":
  unittest.main()
