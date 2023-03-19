# Napisz funkcję, która jako PIERWSZY argument przyjmuje rodzaj operacji
#     "suma", "różnica", "iloczyn"
# a następnie wykona sumowanie/odejmowanie/mnożenie wszystkich argumentów
# podanych po pierwszym. Ilość argumentów do obliczeń może być dowolna

def calculation(option: str, *args) -> float:
    if len(args) >= 2:
        result = args[0]

        if option == "suma":
            for i in range(1, len(args)):
                result += args[i]
        elif option == "różnica":
            for i in range(1, len(args)):
                result -= args[i]
        elif option == "iloczyn":
            for i in range(1, len(args)):
                result *= args[i]

        return result
    else:
        return args[0]


print(calculation("suma", 1, 2, 3))
print(calculation("różnica", 10, 2, 5))
print(calculation("iloczyn", 2, 2, 2))
print(calculation("różnica", -2))
