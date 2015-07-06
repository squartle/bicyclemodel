
class Bicycle(object):
    def __init__(self, model, weight, prod_cost):
        self.model = model
        self.weight = weight
        self.prod_cost = prod_cost

class Shop(object):
    def __init__(self, name, markup, inventory):
        self.name = name
        self.markup = markup
        self.inventory = inventory

    inventory = {}

    def fillInventory(self, ????):
        


    def price(self, Bicycle.model):
        price = (markup + 1) * Bicycle.prod_cost
        print price

    def profit(self, markup, Bicycle()):
        profit = price - prod_cost
        print profit

class Customer(object):
    def __init__(self, firstname, funds, ownership):
        self.firstname = firstname
        self.funds = funds
        self.ownership = ownership

    ownership = ()

    def purchase(self, ):
        if self.funds >= Shop.price:
            self.ownership.append(Bicycle.model)
            self.funds = self.funds - Shop.price
        else:
            print "I can't afford that!"

speedRacer = Bicycle("racing", 12, 220)
beachBum = Bicycle("casual", 34, 159)
urbanCyclist = Bycicle("hybrid", 6, 583)
cruiserClassy = Bicycle("casual", 12, 694)
ultimateArmstrong = Bicycle("racing", 8, 743)
happyHipster = Bicycle("hybrid", 15, 325)

OffRampBikes = Shop("Off Ramp Bicycles", .20, ORBinventory)
pMultiplier = markup + 1
ORBinventory = []

def initInventory():
    for
