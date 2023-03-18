class Car:
    def __init__(self, color, price: float, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []

    def __str__(self):
        return f"{self.brand}, {self.color}, {self.price}"

    def __int__(self):
        return self.price

    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True


c1 = Car("Czerwony", 4500000, "Ferrari")
print(c1)
c1.color = "Srebrny"
print(c1)