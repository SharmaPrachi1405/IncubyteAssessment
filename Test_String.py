import unittest

from StringCalculator import String_Calculator

def return_zero_on_empty_string():
    result = add("")
    assert result == 0, "String calculater should return 0 on empty string"

def return_correct_value_on_one():
    result = add("1")
    assert result == 1, "String calculater should return 1 on \"1\" string"
