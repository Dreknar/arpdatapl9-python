# Napisz program, gdzie użytkownik podaje liczbę n (int)
# Następnie program wyświetla wszystkie liczby parzyste od 0 do n (włącznie)

n = int(input("Podaj liczbę: "))
i = 0
while i <= n:
    print(i)
    i += 2

# Wykorzystując pętle while, program wyświetli wszystkie pierwiastki
#     liczb od 10 do 2 (włącznie) (n ** 0.5)

n = 10
while n >= 2:
    # print("Pierwiastek liczby", n, "to:", n ** 0.5)
    n -= 1

# Napisz program, który sumuje wszystkie liczby całkowite z danego przedziału
# Początek i koniec podaje użytkownik
# Np. start = 10, end = 12, wynik - 33

s = int(input("Podaj start: "))
e = int(input("Podaj koniec: "))
result = 0

for i in range(s, e + 1):
    result += i

print("Wynik", result)
print("Wynik", sum(range(s, e + 1)))