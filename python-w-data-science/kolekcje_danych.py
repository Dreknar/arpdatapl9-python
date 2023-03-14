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
# print(txt[0])       # Wyświetl 1 znak.
# print(txt[:4])      # <0, 4) | <0, 3>
# print(txt[2:8])     # <2, 8) | <2, 7>
# print(txt[3:])      # <3, len) | <3, len-1>
# print(txt[2:8:2])   # <2,7> co drugi = <2,4,6>
# print(txt[::3])     # <cały tekst> co trzeci
# print(txt[::-1])    # Od końca

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
#  fun("Ala ma kota", 10) zwraca -1
#  fun("HELLO", 2) zwraca -3


def reverse_idx(text, index):
    if 0 <= index <= (len(text) - 1):
        return index - len(text)
    else:
        return -999


# print(reverse_idx("HELLO", 0))
# print(reverse_idx("HELLO", 4))
# print(reverse_idx("HELLO", -1))
# print(reverse_idx("HELLO", 10))

# # Lista # #
# values = [3, 4.67, "LOL", True, 11, "XD"] # Nie robić tak!
animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
numbers = [2, 5, 10, 3]
# Pusty lista: empty = [] lub empty = list()

# Metody/Funkcje listy
# print(len(animals))
# print(animals[0], animals[-1], animals[2:4])
# print(sum(numbers), max(numbers), min(numbers))

# Dodawanie
animals.append("Szynszyla")
print(animals)
animals.extend(["Mysz", "Kanarek"])
print(animals)
animals.insert(1, "Krokodyl")
print(animals)

# Usuwanie
animals.remove("Szynszyla")
print(animals)
deleted_args = []

deleted_args.append(animals.pop()) # Jeżeli nie podany idx, usuwamy ostatni element
print(animals)
deleted_args.append(animals.pop(2))
print(animals)
deleted_value = animals.pop(0)
deleted_args.append(deleted_value)
print(animals, deleted_args)

# Modyfikacja
animals[0] = "Mrówka"
print(animals)

# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usun
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usun - wykonujemy pop()
# Funkcja niczego nie zwraca