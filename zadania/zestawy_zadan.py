# Program przyjmuje od użytkownika dwie liczby:
#     1. Liczba prawidłowych odpowiedzi (int)
#     2. Liczba pytań (int)
# Następnie program wyświetla odpowiedni komunikat na konsoli zależnie od % prawidłowych odpowiedzi:
#     100% - 90% : 5.0, 89% - 76% : 4.5, 75% - 70% : 4.0
#     69% - 60% : 3.5, 59% - 50% : 3.0, 49% - 0% : 2.0

# total_answers = int(input("Podaj ilość pytań: "))
# correct_answers = int(input("Podaj ilość prawidłowych odp: "))
#
# result_percent = int((correct_answers / total_answers) * 100)
# if 100 <= result_percent <= 90:
#     print("Ocena: 5.0")
# elif 89 <= result_percent <= 76:
#     print("Ocena: 4.5")
# elif 75 <= result_percent <= 70:
#     print("Ocena: 4.0")
# elif 69 <= result_percent <= 60:
#     print("Ocena: 3.5")
# elif 59 <= result_percent <= 50:
#     print("Ocena: 3.0")
# else:
#     print("Ocena: 2.0")

# Napisz funkcję o nazwie show_temp_status, która przyjmuje jeden argument typu float
# Następnie zwraca str (nie wykonuje print!) zależnie od wartości podanego argumentu:
#     Poniżej 36.4 - wychłodzenie
#     <36.4 36.8> - norma
#     <36.9, 37.1> - stan podgorączkowy
#     Powyżej 37.1 - gorączka

def show_temp_status(temperature):
    if temperature > 37.1:
        return "Gorączka"
    elif 36.9 <= temperature <= 37.1:
        return "Stan podgorączkowy"
    elif 36.4 <= temperature <= 36.8:
        return "Norma"
    else:
        return "Wychłodzenie"


print(show_temp_status(38))
print(show_temp_status(36.6))
print(show_temp_status(36.75))
print(show_temp_status(36.85))
print(show_temp_status(36.2))
print(show_temp_status(float(input("Podaj temperaturę: "))))
