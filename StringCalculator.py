import unittest


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




