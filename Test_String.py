import unittest

from StringCalculator import String_Calculator

def test_string_calc_should_return_zero_on_empty_string():
    result = add("")
    assert result == 0, "String calculater should return 0 on empty string"