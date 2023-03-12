# 1. Użytkownik podaje liczbę, a nastęnie dostaje odpowiedź czy podana liczba
#     jest parzysta/nieparzysta.

x = int(input("Podaj liczbę: "))
if x % 2 == 0:
    print("Liczba parzysta.")
else:
    print("Liczba nieparzysta.")

# 2. Użytkownik podaje liczbę, a nastęnie program:
#     Wyświetli "Pif Paf", jeżeli podana liczba jest podzielna przez 3 i 5
#     Wyświetli "Pif", jeżeli podana liczba jest podzielna tylko przez 3
#     Wyświetli "Paf", jeżeli podana liczba jest podzielna tylko przez 5
#     Wyświetli komunikat "Twoja liczba to: " + podana liczba, jeżeli nie spełniono
#     żadnego z powyższych warunków.

y = int(input("Podaj liczbę: "))

if y % 5 == 0 and y % 3 == 0:
    print("Pif Paf")
elif y % 3 == 0:
    print("Pif")
elif y % 5 == 0:
    print("Paf")
else:
    # print("Twoja liczba to:", y)
    print("Twoja liczba to: " + str(y))
