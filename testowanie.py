from przykladowe_testowanie import *

assert list_power([1, 2, 3]) == [1, 4, 9]
assert list_power([5]) == [25]
assert len(list_power([5])) == 1
assert show_temp_status(36.4) == "OK"
assert show_temp_status(36.8) == "OK"
assert show_temp_status(36.6) == "PERFECT"
assert show_temp_status(30.0) == "NOT OK"
assert show_temp_status(40.0) == "NOT OK"
assert show_temp_status("ALA MA KOTA") == "ERROR"