import unittest

from StringCalculator import String_Calculator

class StringTest(unittest.TestCase):
    def ShouldReturnZeroForEmptyString(self):
        T1 = String_Calculator()
        T1.add("")
        self.assertEquals(0, T1.word)