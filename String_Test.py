import unittest

from StringCalculator import String_Calculator

def return_zero_on_empty_string():
    result = add("")
    assert result == 0, "String calculater should return 0 on empty string"

def return_correct_value_on_one():
    result = add("1")
    assert result == 1, "String calculater should return 1 on \"1\" string"



def should_return_correct_value_on_two():
    result = add("2")
    assert result == 2, "String calculater should return 2 on \"2\" string"

def should_add_two_numbers():
    result = add("1,2")
    assert result == 3, "String calculater should return 3 for \"1,2\" string"

    result = add("5,10")
    assert result == 15, "String calculater should return 15 for \"5,10\" string"

def test_string_calc_negative_number_exception_check():
    try:
        add("1\n-2,3")
    except ValueError as e:
        assert str(e) == "negatives not allowed [-2]"