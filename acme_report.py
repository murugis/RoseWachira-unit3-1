from random import randint, sample, uniform


from acme import Product

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
    name_1 = []
    price_1 = []
    weight_1 = []
    flammability_1 = []

    for product in products:
        name_1.append(product.name)
        price_1.append(product.price)
        weight_1.append(product.weight)
        flammability_1.append(product.flammability)


        name_u = len(name_1)
        avg_p = sum(price_1)/len(price_1)
        avg_w = sum(weight_1)/len(weight_1)
        avg_f = sum(flammability_1)/len(flammability_1)

    print(f'Unique product names: {name_u} ')
    print(f'Average price: {avg_p} ')
    print(f'Average weight: {avg_w} ')
    print(f'Average flammability: {avg_f} ')   


    return name_u, avg_p, avg_w, avg_f    
    

if __name__ == "__main__":
    inventory_report(generate_products())
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
   
    


