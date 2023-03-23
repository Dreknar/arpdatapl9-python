def find_max(numbers: list) -> float:
    try:
        current_max = float(numbers[0])
    except ValueError:
        print("Błędne dane!")
        exit(-999)

    if len(numbers) == 1:
        return current_max
    else:
        for i in range(1, len(numbers)):
            try:
                if current_max < numbers[i]:
                    current_max = float(numbers[i])
            except TypeError:
                continue

        return current_max


n = [1, "C", 6, "A", 2, 3, "B", 2, 3]
x = ["ALA MA KOTA"]
z = ["A", 3, 4, 5, 6, 1]
print(find_max(x))
