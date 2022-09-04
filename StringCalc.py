
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

    def should_return_correct_value_on_two():
        result = add("2")
        assert result == 2, "String calculater should return 2 on \"2\" string"

    def should_add_two_numbers():
        result = add("1,2")
        assert result == 3, "String calculater should return 3 for \"1,2\" string"

        result = add("5,10")
        assert result == 15, "String calculater should return 15 for \"5,10\" string"

    def validate_numbers(param: str):
        if any(num < 0 for num in param):
            raise ValueError("negatives not allowed " + str([num for num in param if num < 0]))



