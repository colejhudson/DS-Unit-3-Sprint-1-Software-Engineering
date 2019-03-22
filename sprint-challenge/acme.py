import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        price_per_unit = self.price/self.weight

        if price_per_unit < 0.5:
            return "Not so stealable..."
        elif 0.5 <= price_per_unit < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        explodability = self.flammability * self.weight

        if explodability < 10:
            return "...fizzle."
        elif 10 <= explodability < 50:
            return "...boom!"
        else:
            return "...BABOOM!"
