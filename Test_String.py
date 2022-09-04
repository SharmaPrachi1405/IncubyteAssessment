from asyncio.tasks import _T1
import unittest

from StringCalculator import String_Calculator

class StringTest(unittest.TestCase):
    def ShouldReturnZeroForEmptyString(self):
        T1 = String_Calculator()
        result = T1.add("")
        self.assertEquals(0, result)

    
    def ShouldReturnOneForString(word , expectedresult,self):
        test_list = {"1",1, "2",2}
        T1 = String_Calculator()
        result = T1.add("1")
        for word, expectedresult in test_list:
            with self.subTest():
                self.assertEquals(expectedresult, result)

    def ShouldReturnSumForString(self, word , expectedresult):
        T1 = String_Calculator()
        result = T1.add(word)
        self.assertEquals(expectedresult, result)


    def NumberNegativeThan(  self ,word):
        T1 = String_Calculator()
        result = T1.add(word)
        para_list = [-1, 0]
        for i in para_list:
            if(i<0):
                return 0
        self.assertLess(word<0, "Positive number expected")

    
    def MultipleNegatives(self , word):
        Negative_list=[0,-1,-2]
        T1=String_Calculator()
        result = T1.add(word)
        for i in Negative_list:
           if(i<0):
            print(i)
            self.assertIn(i<0, "Negative numbers")

    def NumberBiggerThan( word , expectedresult, self):
        T1 = String_Calculator()
        result = T1.add(word)
        for i in word :
            if(word > 1000):
                temp = word
                i+=1
        self.assertEquals(expectedresult, result)