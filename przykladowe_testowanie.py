def show_temp_status(temp: float) -> str:
    try:
        if 36.4 <= temp <= 36.8:
            if temp == 36.6:
                return "PERFECT"
            else:
                return "OK"
        else:
            return "NOT OK"
    except TypeError:
        return "ERROR"


def list_power(numbers: list) -> list:
    result = []
    for i in numbers:
        result.append(i ** 2)
    return result


assert list_power([1, 2, 3]) == [1, 4, 9]
assert list_power([5]) == [25]
assert len(list_power([5])) == 1
assert show_temp_status(36.4) == "OK"
assert show_temp_status(36.8) == "OK"
assert show_temp_status(36.6) == "PERFECT"
assert show_temp_status(30.0) == "NOT OK"
assert show_temp_status(40.0) == "NOT OK"
assert show_temp_status("ALA MA KOTA") == "ERROR"