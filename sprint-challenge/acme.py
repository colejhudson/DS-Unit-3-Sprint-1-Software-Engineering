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

class BoxingGlove(Product):
    def __init__(self, *args, weight=10, **kwargs):
        super().__init__(*args, weight=weight, **kwargs)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
