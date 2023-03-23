result = {}

with open("dane_20230323_processing.txt", "r", encoding="utf-8") as file:
    for line in file:
        tmp = line.replace("\n", "").split(";")
        key = tmp[0]
        value = tmp[3]

        if key not in result.keys():
            result[key] = value
        elif result[key] < value:
            result[key] = value

for i in result:
    print(i, result[i])
