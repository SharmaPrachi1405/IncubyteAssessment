import unittest

from StringCalculator import String_Calculator

class StringTest(unittest.TestCase):
    def ShouldReturnZeroForEmptyString(self):
        T1 = String_Calculator()
        result = T1.add("")
        self.assertEquals(0, result)

    test_list = ["1",1]
    def ShouldReturnOneForString(self, word , expectedresult):
        T1 = String_Calculator()
        result = T1.add(word)
        self.assertEquals(expectedresult, result)

    def ShouldReturnSumForString(self, word , expectedresult):
        T1 = String_Calculator()
        result = T1.add(word)
        self.assertEquals(expectedresult, result)