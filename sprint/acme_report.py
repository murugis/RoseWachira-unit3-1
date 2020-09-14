from sprint.acme import Product
from random import randint, sample, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    alist=ADJECTIVES + NOUNS
    num_products = random.sample(alist,30)
    products= products.append(num_products)

    # TODO - your code! Generate and add random products.
    '''
    This is a function that generate random sample products 

    returns products
    '''
    
    return products

def inventory_report(products):
    price= randomint(5,100)/100
    weight = random.int(5,100)/100
    flammability = random.random(0.0,,2.5)

    print("Average price:", price)
    print("Average weight:",weight)
    print("Average flammability",flammability)
    


if __name__ == '__main__':
    inventory_report(generate_products())
```