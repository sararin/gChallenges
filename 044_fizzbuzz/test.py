import unittest
import fizzbuzzer as fber

class TestCode(unittest.TestCase):
  def test_fizzerbuzzer(self):
    self.assertEqual(fber.fizzerbuzzer(7), "1 2 Fizz 4 Buzz Fizz")
    self.assertEqual(fber.fizzerbuzzer(16), "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz")

if __name__ == "__main__":
  unittest.main()
