with open("surnames.txt", "w", encoding="utf-8") as file:
    file.write("Kowalski\n")
    file.write("Nowak\n")
    file.write("Brzechwa\n")
    file.writelines(("Malinowski\n", "Morawiecki\n", "Killer"))


from random import randint
print(randint(1, 49))

# Użytkownik podaje ilość losowań (n), a następnie program zapisuje
# do pliku n przykładowych wyników lotto
# * Pomijaj duplikaty w losowaniu
#
# Przykład: użytkownik podaje n = 2
# Wynik (zawartość pliku):
#
# 2 6 12 40 31 22
# 12 34 49 21 1 12