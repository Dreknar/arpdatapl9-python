n = int(input("Podaj liczbę: "))
summary = 0

while n >= 0:
    summary += n
    n = int(input("Podaj liczbę: "))

print(f"Suma podanych liczb to: {summary}")
