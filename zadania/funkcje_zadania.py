# 1. Napisz funkcję is_even, która przyjmuje jeden argument
#     A następnie zwraca True - jeżeli liczba jest parzysta,
#     w przeciwnym razie False
#
#     Wykorzystaj nową funkcję do poprzedniego zadania
#     (tam gdzie użytkownik podawał liczbę, a następnie otrzymywał komunikat
#      liczba parzysta/nieparzysta)

def is_even(x):
    return x % 2 == 0


y = 11
if is_even(y):
    print("Parzysta")

# 2. Napisz funkcję my_pow, która pozwoli na zwrócenie potęgi wybranej liczby
#     do wybranej potęgi. Liczbe oraz potegę podajemy jako argumenty do tej fukncji


def my_pow(base, power):
    return base ** power


z = my_pow(2, 10)
print(z)
