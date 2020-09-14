
from random import randint, sample, uniform



from sprint.acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for products in range(num_products=30):
        adjective = sample(ADJECTIVES,1)[0]
        noun = sample(NOUNS,1)[0]

        name = adjective + " " + noun

        price= randint(5,100)
        weight = randint(5,100)
        flammability = uniform(0.0,2.5)

        prod2 = Product(name,price,weight,flammability)
        products.append(prod2)


    
    return products



def inventory_report(products):
    name_1 = []
    price_1 = []
    weight_1= []
    flammability_1 = []

    for product in products:
        name_1.append(products.name)
        price_1.append(products.price)
        weight_1.append(products.weight)
        flammability_1.append(products.flammability)
    
    uname = []

   

    
    uname = len(name_1)
    avg_p = sum(price_1)/len(price_1)
    avg_w = sum(weight_1)/len(weight_1)
    avg_f = sum(flammability_1)/len(flammability_1)

        

if __name__ == "__main__":
    inventory_report(generate_products())
    
    
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    uname.inventory_report()
    print(f'Unique product names: {uname}')
    avg_p.inventory_report()
    print(f'Average price: {avg_p}')
    print(f'Average weight: {avg_w}')
    print(f'Average flammability: {avg_f}')
    