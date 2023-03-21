with open("surnames.txt", "w", encoding="utf-8") as file:
    file.write("Kowalski\n")
    file.write("Nowak\n")
    file.write("Brzechwa\n")
    file.writelines(("Malinowski\n", "Morawiecki\n", "Killer"))

