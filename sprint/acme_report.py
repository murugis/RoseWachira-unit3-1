from random import randint, sample, uniform


from sprint.acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    The function generates 30 random products and them as a list[]
    '''
    products = []
    for products in range(num_products=30):
        adjective = sample(ADJECTIVES, 1)[0]
        noun = sample(NOUNS, 1)[0]

        name = adjective + " " + noun

        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)

        prod2 = Product(name, price, weight, flammability)
        products.append(prod2)
    return products   

def inventory_report(products):   
    '''
    This function generates an invetory report of the products.
    returns:
    unique product names
    average mean
    average weight
    average flammability
    '''
    name_1 = [products.name]
    price_1 = [products.price]
    weight_1 = [products.weight]
    flammability_1 = [products.flammability]
    print(len(name_1))
    print(sum(price_1)/len(price_1))
    print(sum(weight_1)/len(weight_1))
    print(sum(flammability_1)/len(flammability_1))

if __name__ == "__main__":
    inventory_report(generate_products())
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: ')
    print(f'Average price: ')
    print(f'Average weight: ')
    print(f'Average flammability: ')
    