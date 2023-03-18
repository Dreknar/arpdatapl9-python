# Napisz klasę Animal, która zawiera pola:
#     - legs_count (float)
#     - eyes_count (float)
#     - name (str)
#     - is_alive (Zawsze domyślne True - dla każdego obiektu)
#
# Dopisz do niej funkcje:
#     __str__ - zwraca nazwę zwierzątka

class Animal:
    def __init__(self, legs_count, eyes_count, name, weight):
        self.legs_count = legs_count
        self.eyes_count = eyes_count
        self.name = name
        self.is_alive = True
        self.weight = weight

    def __str__(self):
        return self.name

    def running(self):
        print(f"{self.name} - Tup tup tup tup tup")


class Dog(Animal):
    def __init__(self, legs_count, eyes_count, name, weight, race):
        super().__init__(legs_count, eyes_count, name, weight)
        self.race = race

    def __str__(self):
        return f"{super().__str__()} - {self.race}"


d1 = Dog(4, 2, "Burek", 30, "Husky")
print(d1.is_alive, d1.race)
d1.running()
