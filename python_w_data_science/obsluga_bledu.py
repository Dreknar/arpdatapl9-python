def dec_to_bin(value: int) -> list:
    parts = []

    while value != 0:
        parts.append(value % 2)
        value //= 2

    return parts[::-1]


x = 10

try:
    print(x / 0)
except ZeroDivisionError:   # expect: <-- instrukcje dla wystąpienia dowolnego błędu
    print("Próbowałeś/aś dzielić przez zero.")
finally:
    # Wykonaj to zawsze na końcu - niezależnie od powyższych bloków
    print("WYKONAŁEM SIĘ!")

a = [10, 20, 3, 4, "Ala ma kota", True, 3, 4, 12, "Piesek", "XD", 20]
errors_value = []

for i in range(len(a)):
    try:
        a[i] = dec_to_bin(a[i])
    except TypeError:
        errors_value.append(a[i])


