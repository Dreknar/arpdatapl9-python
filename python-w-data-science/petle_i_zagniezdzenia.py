accounts = [
    ("A001", "100600", 250.50),
    ("B001", "200800", 1999.97),
    ("A002", "600100", 62780.00)
]

# Dla przykładu powyżej:
#             0       1       2
#     0   [0][0]  [0][1]  [0][2]
#     1   [1][0]  [1][1]  [1][2]
#     2
# print(accounts)
# print(accounts[0][2], accounts[1][2])

# Pętle for
# 1. Łańcuch znakowy
# for c in "KOTEK":
#     print("Litera:", c)

# 2. Łańcuch znakowy -> lista
# for word in "Ala ma kota".split(" "):
#     print("Słowo:", word)

# 3. Lista/Krotka
# for element in accounts:
#     print("Klient:", element)

# 4. Ciag liczb (range)
# range(start, end, step) | <start, end-1>
# Domyślnie krok = 1
# range(10) - <0,9>
# range(1,12) - <1,11>
# range(2,10,2) - <2,9> z krokiem 2

# for i in range(2, 10, 3):
#     print("Liczba:", i)

# 4a. Ciąg malejący
# for i in range(10, -1, -1):
#     print(i)

# Mamy listę danych:
# data = [
#     ("Adam", 750),
#     ("Ewa", 250),
#     ("Jakub", 200),
#     ("Elżbieta", 1000),
#     ("Adam", 400),
#     ("Ewa", 300)
# ]
#
# Należy przepisać powyższe krotki do słownika danych według poniższego schematu:
#     klucz - 1 wartość krotki
#     wartość - 2 wartość krotki podzielona przez 50
#
#     Przykładowo dla pierwsze elementu listy powinnyśmy otrzymać wpis:
#     "Adam": 15
#
#     Program ma pomijać klucze które są duplikowane (wchodzi pierwsze wystąpienie),
#     czyli drugi "Adam" powinien być pominięty w przetwarzaniu.

data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300),
    ("Bożydar", 100)
]

data_in_dict = {}

print(data[0][0], data[0][1])

for i in range(len(data)):
    if data[i][0] not in data_in_dict.keys():
        data_in_dict[ data[i][0] ] = data[i][1] // 50

print(data_in_dict)


# Napisz funkcję, która przyjmuja łańcuch znakowy
#     (dla ułtawienia: same małe litery)
# Przykładowo: alamakotaakotmapierdolca
# Funkcja ma zwrócić słownik (return), który zawiera informacje w postaci:
#     Klucz - litera
#     Wartość - ilość wystąpień litery w tekście
# Przykładowo: dla klucza "l" wartości to 2

txt = "alamakotaakotmapierdolca"

def char_counter(text: str) -> dict:
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = text.count(c)

    return result

def char_counter_alternative(text: str) -> dict:
    result = {}
    for c in text:
        if c in result.keys():
            result[c] += 1
        else:
            result[c] = 1

    return result


print(char_counter(txt))
print(char_counter_alternative(txt))
