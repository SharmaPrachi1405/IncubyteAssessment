import unittest

from StringCalculator import String_Calculator

class StringTest(unittest.TestCase):
    def ShouldReturnZeroForEmptyString(self):
        T1 = String_Calculator()
        result = T1.add("")
        self.assertEquals(0, result)

    test_list = {"1",1, "2",2}
    def ShouldReturnOneForString(word , expectedresult,self):
        T1 = String_Calculator()
        result = T1.add("1")
        for word, expectedresult in test_list:
            with self.subTest():
                self.assertEquals(expectedresult, result)

    def ShouldReturnSumForString(self, word , expectedresult):
        T1 = String_Calculator()
        result = T1.add(word)
        self.assertEquals(expectedresult, result)


    def NumberNegativeThan( word , expectedresult, self):
        T1 = String_Calculator()
        result = T1.add(word)
        self.assertEquals(word<0, "Positive number expected")

    def NumberBiggerThan( word , expectedresult, self):
        T1 = String_Calculator()
        result = T1.add(word)
        for i in word :
            if(word > 1000):
                temp = word
                i+=1
        self.assertEquals(expectedresult, result)