a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

print(f"Największa wartość to: {max([a, b, c])}")

if a == b and b == c:
    print("Liczby są takie same")
elif a == b:
    print("A i B są takie same")
elif a == c:
    print("A i C są takie same")
elif b == c:
    print("B i C są takie same")
else:
    print("Liczby są różne")
