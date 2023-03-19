try:
    print(10 / 0)
    print("Ala ma " + 5 + "kotów.")
except ZeroDivisionError:
    print("Próbowano dzielić przez zero")
except TypeError:
    print("Wystąpił problem z typem danych")

# Do zadania nr 4 z pracy domowej dopisz zabezpeczenie, jeżeli użytkownik poda
# informację, której nie można konwertować na int

try:
    n = int(input("Podaj liczbę: "))
    summary = 0

    while n >= 0:
        summary += n
        n = int(input("Podaj liczbę: "))

    print(f"Suma podanych liczb to: {summary}")

except ValueError:
    print("Podano błędną informację")





# Rozwiń funkcjonalność zadania z (opcja, *args) o nową opcję "iloraz".
# Zabezpiecz program, że w przypadku dzielenia przez zero kontynuuj działanie
# iloraz (dzielenia kolejnych wartości), pomijając błędny (umieść continue w except)

