# 1. Napisać program, który przyjmie od użytkownika dwie wartości zmiennoprzecinkowe (float)
#     a nastęnie wyświetli ich: sumę, różnicę oraz iloczyn

first_num = float(input("Podaj I liczbę: "))
second_num = float(input("Podaj II liczbę: "))
print("Dodawanie:", first_num + second_num)
print("Odejmowanie:", first_num - second_num)
print("Mnożenie:", first_num * second_num)

# 2. Napisać program, który przyjmie od użytkownika tekst jako "nazwę produktu" oraz
#     jego ilośc a następnie wyświetli komunikat w formacie:
#     produkt - ilość
#
#     Przykładowo: podano "CPU" oraz 10
#     Wynik: CPU - 10

txt = input("Podaj produkt: ")
amount = input("Podaj ilość: ")
print(txt, "-", amount)
print(txt + " - " + amount)
