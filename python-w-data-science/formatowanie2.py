# fprint z zaokrągleniem (formatowanie)
value = 3.98777773
c = 200
print(f"Wartość: {value:6.2f}") # Value zajmuje 6 miejsc (z kropką), 2 po przecinku
print(f"Wartość: {value:.2f}")
print(f"Wartość: {c:4d}")

# ---------------------------------------
print("--------------------------")
print(f"A: {100:10d}")
print(f"B: {2500:10d}")
print(f"C: {1000000000:10d}")
print("--------------------------")
