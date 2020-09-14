import random

class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randrange(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''
        This calculates the price of the Product divided by the weight

        returns a message:
        if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0
        return "Kinda stealable.",
        and otherwise return "Very stealable!"
        '''
        stealability = self.price/self.weight

        if stealability < 0.5:
            print('Not so stealable')

        elif stealability > 0.5 and stealability <= 1:
            print('Kinda stealable') 
        else:
            print('Very stealable')

    def explode(self):
        '''
        This is a function that calculates the flammability times the weight, 
        and returns a message: 
        if the product is less than 10 return "...fizzle.", 
        if it is  greater or equal to 10 but less than 50
        return "...boom!", and otherwise
        return "...BABOOM!!"
        '''
        boom = self.flammability*self.weight

        if boom < 10:
            print("fizzle")

        elif boom >= 10 and boom < 50:
            print("Boom!")
        else:
            print("BABOOM!!!")

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randrange(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)
        self.weight = weight

    def explode(self):
        print('... it is a glove')

    def punch(self):

        '''
        This is a function that calculates the flammability times the weight, and then
        returns a message:

        if the product is less than 10 return "...fizzle.",
        if it is  greater or equal to 10 but less than 50
        return "...boom!", and otherwise
        return "...BABOOM!!"
        '''

        if self.weight < 5:
            print("That tickles")

        elif self.weight >= 5 and self.weight < 15:
            print("Hey that hurts!")
        else:
            print("OUCH!!!")

     


        


    