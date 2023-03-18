# Warunki arytmetyczne
cost = 3.10
product = "cebula"

if cost >= 3:
    print("Nie kupuj, bo za drogie!")
else:
    print("Kupuj bo tanio!")

# Operatory: not, and, or
if product == "cebula" and cost < 3:
    print("Kupuj tę cebulę, Polaku!")
else:
    print("Unikaj jak ognia, bo Panieee jakie drogie!")

# Operator in / not in (później) oraz przedziały
# Przypadek: Oceny są z zakresu 2.0 do 5.0
grade = 5.2

if 2 <= grade <= 5:
    print("Ocena prawidłowa")
else:
    print("Ocena nieprawidłowa")

# elif - sprawdza kolejny warunek, jak poprzedni był nieprawdziwy
cost = 2.99
product = "marchewka"

if product == "cebula" and cost <= 3:
    print("Kupujesz cebulę")
elif product == "marchewka" and cost <= 4.5:
    print("Kupujesz marchewkę")
elif product == "wódka" and cost <= 19.99:
    print("Kupujesz alkohol.")
else:
    print("Wychodzisz bez zakupów.")