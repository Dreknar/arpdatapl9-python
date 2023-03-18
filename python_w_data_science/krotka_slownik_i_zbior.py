# Słownik
contacts = {
    "Adam": "670210999",
    "Ewelina": "123870456",
    "Piotr": "000222666"
}

# print(len(contacts))
# Dostęp do kluczy, wartości, elementów
# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())

if "Iza" in contacts.keys():
    print("Kontakt istnieje.")

# Dodawanie nowych kluczy | Modyfikacja wartości
# contacts["Iza"] = "123321312"
# print(contacts)
# contacts["Adam"] = "000000000"
# print(contacts)

# Wyświetlenie wybranej wartości
# print(contacts["Ewelina"])

# 1
# print(contacts.get("Bożydar", -1))

# 2
if "Bożydar" in contacts.keys():
    print(contacts["Bożydar"])
else:
    print(-1)

# Usuwanie kluczy (oraz ich wartości)
contacts.pop("Adam") # W tym przypadku pop nie może być bez arg.
# Przepisywanie pod nowy klucz
contacts["Mateusz"] = contacts.pop("Ewelina")
# del contacts["Iza"] # Dla ciekawskich
# print(contacts)

# Napisz funkcję o nazwie add_contacts, która przyjmuje następujące argumenty:
#     - słownik z kontaktami (dict)
#     - nazwę klucza (str)
#     - nr telefonu (str)
# Następnie funkcja wypisuje na konsoli komunikat:
#     - "Kontakt dodano", jeżeli dodaliśmy kontakt + dodajemy kontakt. :)
#     - "Kontakt istnieje", jeżeli podany klucz istnieje w słowniku
# Funkcja niczego nie zwraca (nie używamy z return)


def add_contacts(con_dict: dict, key: str, value: str) -> None:
    if key in con_dict.keys():
        print("Kontakt istnieje")
    else:
        con_dict[key] = value
        print("Kontakt dodano")


contacts2 = {
    "Ewa": "000111222"
}

# add_contacts(contacts2, "Ewa", "123456789")
# add_contacts(contacts2, "Adam", "123456789")

# Krotka (tuple)
metadata = ("Python w DS", "1.0", "20230315", "20230315")
# print(metadata)
# print(metadata[0], metadata[3], len(metadata))
# print(metadata.count("20230315"))

# Zbiór
numbers = {1, 2, 3, 5, 5, 6, 7, 1, 2, 3}
# Pusty zbiór: n = set()
print(numbers)
numbers.add(9) # Dodanie pojedynczego elemntu
numbers.update([1, 4, 5, 2, 0, 11]) # Dodanie listy elementów
numbers.update(["a", "b", "c"])
print(numbers)
