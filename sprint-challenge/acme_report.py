import acme, random

def generate_products(n_products=30):
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

    return [
            acme.Product(
                random.choice(adjectives)+random.choice(nouns), 
                price=random.randint(5, 100), 
                weight=random.randint(5, 100), 
                flammability=random.uniform(0.0, 2.5)
            ) 
            for _ in range(n_products)
        ]

def mean(xs):
    return sum(xs)/len(xs)

def inventory_report(products):
   names = [product.name for product in products]
   prices = [product.price for product in products]
   weights = [product.weight for product in products]
   flammables = [product.flammability for product in products]

   unique_name_count = len(set(names))

   print(
       ("ACME CORPORATION OFFICIAL INVENTORY REPORT\n" +
       "Unique product names: {}\n" + 
       "Average price: {}\n" + 
       "Average weight: {}\n" + 
       "Average flammability: {}").format(
           unique_name_count, 
           mean(prices), 
           mean(weights), 
           mean(flammables)
        )
   )

if __name__ == '__main__':
    inventory_report(generate_products())
