# Napisać klasę Person, która zawiera pola:
#     - imie (str)
#     - nazwisko (str)
#     - adres (str)
#     - wiek (int)
# Dodatkowo klasa posiada metody:
#     - __str__ - zwraca tekst w formacie: "Nazwisko, Imie, adres"
#     - check_is_adult() - zwraca true, jeżeli wiek >= 18
#
# Napisać klasę Customer, która dziedziczy po Person, a dodatkowo:
# Posiada pola:
#     - orders (list)
#     - login (str)
#     - total_order_cost (float)
# Oraz funkcje:
#     - str - wykorzystuje dziedziczony str, a dodatkowo na początku podaje login
#     - add_order(product, cost) - dodaje krotke do listy zamowien
#         Można dodać zamówienie tylko jak użytkownik jest pełnoletni
#         Dodatkowo aktualizuje wartość total_order_cost po dodaniu zamówienia
#     - show_orders() - wyświetla wszystkie zamówienia (jeden pod drugim)

class Person:
    def __init__(self, first_name: str, last_name, address, age):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age

    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.address}"

    def check_is_adult(self):
        return self.age >= 18


class Customer(Person):
    def __init__(self, first_name: str, last_name, address, age, login):
        super().__init__(first_name, last_name, address, age)
        self.login = login
        self.orders = []
        self.total_order_cost = 0.0

    def __str__(self):
        return f"{self.login} - {super().__str__()}"

    def add_order(self, product: str, cost: float) -> None:
        if super().check_is_adult():
            self.orders.append((product, cost))
            self.total_order_cost += cost
        else:
            print("Osoba nie jest pełnoletnia.")

    def show_orders(self):
        for e in self.orders:
            print(e)

