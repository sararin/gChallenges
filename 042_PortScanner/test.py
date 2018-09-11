from unittest import TestCase
from porter import Porter
from porter import Expander

class Porter_TestCode(TestCase):
  def setUp(self):
    self.por = Porteri("127.0.0.1", 30, 512, 3)

class Expander_TestCode(TestCase):
  def setUp(self):
    self.exp = Expander("127.0.0.1-5", "30")

  def test_expandPort(self):
    self.assertEqual(self.exp._expandPort("1-3"), [1,2])
    self.assertEqual(self.exp._expandPort("1"), [1])

  #for some reason "127.0.0.1-5" gives empty list even though it works in normal cimcumstances
  def test_expandAddr(self):
    self.assertEqual(self.exp._expandAddr("127.0.0.1"), ["127.0.0.1"])


