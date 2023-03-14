# # Łańcuch znakowy jako kolekcja danych # #
txt = "Ala ma kota."

# Warunek na podstawie zbioru
if "pies" in txt:
    print("Ala faktycznie posiada kota.")

# Metody dla str
# print(len(txt))
# print(txt.upper())
# print(txt.lower())
# print(txt.isalnum())
# Powielanie tekstu
# print(txt * 2)

# Indeksowanie | 0..(len - 1)
print(txt[0])       # Wyświetl 1 znak.
print(txt[:4])      # <0, 4) | <0, 3>
print(txt[2:8])     # <2, 8) | <2, 7>
print(txt[3:])      # <3, len) | <3, len-1>
print(txt[2:8:2])   # <2,7> co drugi = <2,4,6>
print(txt[::3])     # <cały tekst> co trzeci
print(txt[::-1])    # Od końca

#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -3 -2 -1

# Napisz funkcję, która zwróci "odwrotny" indeks wybranego indeksu i tekstu
#     Przyjmowane argumenty:
#     - łańcuch znakowy
#     - indeks (z przedziału podanego tekstu)
#     Zwraca:
#     - odwrotny indeks
#
#  Przykładowo:
#  fun("Ala ma kota", 11) zwraca -1
#  fun("HELLO", 2) zwraca -3