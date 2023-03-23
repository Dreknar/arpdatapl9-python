with open("dane_20230323.txt", "r", encoding="utf-8") as file:
    with open("dane_20230323_processing.txt", "a", encoding="utf-8") as output:
        for line in file:
            tmp = line.replace("\n", "").split(";")
            row = tmp[0][:2] + ";" \
                  + tmp[1] + ";" + tmp[2] \
                  + ";" + str(round(float(tmp[1]) * float(tmp[2]), 2)) + "\n"
            output.write(row)
