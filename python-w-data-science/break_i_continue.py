# Obie instrukcje działają dla while oraz for
for i in range(1):
    print("I:", i, "Potęga:", 2 ** i)
    if i == 5:
        continue
    print("--- --- --- --- --- ---")

n = 10
while n > 0:
    if n == 4:
        break
    print("n =", n)
    n -= 1
print("Koniec")