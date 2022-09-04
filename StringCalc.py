
from ast import Num
from os import remove


class String_Calculator:
    def add(param: str) -> int:
        param = normalize_delimiters(param)
        if param:
            result = add_numbers(param)
            return result
        else:
            return len(param)

    def normalize_delimiters(param: str) -> str:
        param = normalize_custom_delimiter(param)
        return param.replace("\n", ",").strip(',')

    def add_numbers(param: str) -> int:
        numbers = list(map(int, param.split(",")))
        validate_numbers(numbers)
        return sum(numbers)

    def validate_numbers(param: str):
        if any(num < 0 for num in param):
            raise ValueError("negatives not allowed " + str([num for num in param if num < 0]))

    def Multiple_Negative(param: str):
        if any(num < 0 for num in param):
            return param

    def GreaterThan_Num(param: str):
        if(num > 1000 for num in param):
            remove(num)

