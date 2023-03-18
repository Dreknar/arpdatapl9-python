class Car:
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []

    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True


c1 = Car("Czerwony", 4500000, "Ferrari")
c2 = Car("Zielony", 75000, "Opel")
print(c1.color, c2.color)
print(c1.running, c2.running)
c1.switch()
print(c1.running)
