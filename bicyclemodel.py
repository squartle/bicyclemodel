
class Bicycle(object):
    def __init__(self, model, weight, prod_cost):
        self.model = model
        self.weight = weight
        self.prod_cost = prod_cost

class Shop(object):
    def __init__(self, name, markup):
        self.name = name
        self.markup = markup
        self.inventory = {}
        self.profits = 0

    def stock(self, bicycles):
        for bicycle in list:
            price = (markup + 1) * Bicycle.prod_cost
            self.inventory[bicycle] = price

    def sell(self, Bicycle):
        self.profits += price - Bicycle.prod_cost
        del self.inventory[Bicycle]

class Customer(object):
    def __init__(self, firstname, funds):
        self.firstname = firstname
        self.funds = funds
        self.ownership = ()

    def purchase(self, Bicycle):
        if self.funds >= Shop.price:
            self.ownership.append(Bicycle.model)
            self.funds = self.funds - Shop.price
            sell.Shop(Bicycle)
        else:
            print "I can't afford that!"

speedRacer = Bicycle("racing", 12, 220)
beachBum = Bicycle("casual", 34, 159)
urbanCyclist = Bycicle("hybrid", 6, 583)
cruiserClassy = Bicycle("casual", 12, 694)
ultimateArmstrong = Bicycle("racing", 8, 743)
happyHipster = Bicycle("hybrid", 15, 325)

OffRampBikes = Shop("Off Ramp Bicycles", .20)
MikesBikes = Shop("Mike's Bikes", .33)
