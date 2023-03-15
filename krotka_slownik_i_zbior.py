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
contacts["Iza"] = "123321312"
print(contacts)
contacts["Adam"] = "000000000"
print(contacts)

# Wyświetlenie wybranej wartości
print(contacts["Ewelina"])

# 1
print(contacts.get("Bożydar", -1))

# 2
if "Bożydar" in contacts.keys():
    print(contacts["Bożydar"])
else:
    print(-1)

# Usuwanie kluczy (oraz ich wartości)
contacts.pop("Adam") # W tym przypadku pop nie może być bez arg.
# Przepisywanie pod nowy klucz
contacts["Mateusz"] = contacts.pop("Ewelina")
del contacts["Iza"] # Dla ciekawskich
print(contacts)