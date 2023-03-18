# Obie instrukcje działają dla while oraz for
# for i in range(1):
#     print("I:", i, "Potęga:", 2 ** i)
#     if i == 5:
#         continue
#     print("--- --- --- --- --- ---")

# n = 10
# while n > 0:
#     if n == 4:
#         break
#     print("n =", n)
#     n -= 1
# print("Koniec")

# Lista składana
numbers = []
for i in range(11):
    numbers.append(2 ** i)
print(numbers)
# ==
numbers_v2 = [2 ** i for i in range(11)]
print(numbers_v2)

# Ciekawostka słownik składany
power_for_2 = {i: 2 ** i for i in range(11)}
print(power_for_2)
