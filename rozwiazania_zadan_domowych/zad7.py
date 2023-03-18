n = int(input("Ile danych chcesz podać?: "))
my_collection = set()

for i in range(n):
    txt = input(f"Podaj txt {i+1}: ")
    my_collection.add(txt)

print(f"Ilość unikatowych wartości: {len(my_collection)}")