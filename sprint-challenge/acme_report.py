import random
import acme

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(n_products=30):
    products = []

    for _ in range(n_products):
        name = random.choice(ADJECTIVES)+' '+random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        product = acme.Product(name, price, weight, flammability) 
        products.append(product)

    return products

def mean(values):
    return sum(values)/len(values)

def inventory_report(products):
    names = [product.name for product in products]
    prices = [product.price for product in products]
    weights = [product.weight for product in products]
    flammables = [product.flammability for product in products]

    unique_name_count = len(set(names))

    banner = [
        "ACME CORPORATION OFFICIAL INVENTORY REPORT",
        "Unique product names: {}",
        "Average weight: {}",
        "Average weight: {}",
        "Average flammability: {}"
    ]
    
    print('\n'.join(banner).format(unique_name_count, mean(prices), mean(weights), mean(flammables)))

if __name__ == '__main__':
    inventory_report(generate_products())
