def word_counter(txt: str) -> dict:
    result = {}
    for word in txt.lower().split(" "):
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result


print(word_counter("Ala ma kota Kota kota"))

# Dlaczego nie używamy count?
txt2 = "Ala ma kota kot"
print(txt2.count("kot"), txt2.count("kota"))
