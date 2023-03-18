# Napisz klasę Student, która posiada pozycje/argumenty:
#     - imię (str)
#     - nazwisko (str)
#     - lista ocen (list)
#     - średnia ocena (float)
#
# Powyższe zmienne są definiowane za pomocą __init__. Dla każdego nowego obiektu
# klasy Student lista ocena jest pusta, a średnia równa się 0.0
#
# Dodatkowo dopisz funkcję add_grade, która pozwala dodawać do listy ocenę
# ze zbioru (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0) oraz po dodaniu oceny
# automatycznie przelicza średnią.

# Dodać magic functions:
#     - dla str, aby wyświetlić studenta w formacie: "Imie nazwisko - średnia"
#     - dla int - suma ocen
#     - dla float - srednia ocen

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
        self.avg_grade = 0.0

    def add_grade(self, grade):
        if grade in (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0):
            self.grades.append(grade)
            self.avg_grade = sum(self.grades) / len(self.grades)
            print("Dodano ocenę")
        else:
            print("Ocena nieprawidłowa")


s1 = Student("Jan", "Kowalski")
print(s1.first_name, s1.grades, s1.avg_grade)
s1.add_grade(5.0)
s1.add_grade(2.3)
s1.add_grade(4.0)
print(s1.first_name, s1.grades, s1.avg_grade)
