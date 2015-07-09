class Bicycle(object):
    def __init__(self, name, model, weight, prod_cost):
        self.name = name
        self.model = model
        self.weight = weight
        self.prod_cost = prod_cost

class Shop(object):
    def __init__(self, name, markup):
        self.name = name.upper()
        self.markup = markup
        self.inventory = {}
        self.profits = 0

    def stock(self, list):
        for i in list:
            price = self.markup * i.prod_cost
            self.inventory[i] = round(price, -1)
        print "%s SAYS: Here's our inventory: " % self.name
        for i in self.inventory.iterkeys():
            print i.name

    def sell(self, i):
        self.profits += self.inventory[i] - i.prod_cost
        del self.inventory[i]
        print "%s SAYS: Our profits are $%s. This is what we have left in stock: " %(self.name, self.profits)
        for i in self.inventory.iterkeys():
            print i.name

class Customer(object):
    def __init__(self, name, funds):
        self.name = name.upper()
        self.funds = funds
        self.ownership = []
        self.affordable = []

    def pricecheck(self, Shop):
        for i in Shop.inventory:
            if self.funds >= Shop.inventory[i]:
                self.affordable.append(i)
                print "%s SAYS: The %s is right in the range I'm looking for." %(self.name, i.name)
            else:
                print "%s SAYS: I can't afford the %s!" %(self.name, i.name)

    def purchase(self, Shop):
        import random
        chosen = random.choice(self.affordable)
        self.ownership.append(chosen)
        self.funds -= Shop.inventory[chosen]
        print "%s SAYS: I have $%s leftover and I just bought the %s, which cost %s. " %(self.name, self.funds, chosen.name, Shop.inventory[chosen])
        Shop.sell(chosen)

speedRacer = Bicycle("Speed Racer", "racing", 12, 220)
beachBum = Bicycle("Beach Bum", "casual", 34, 129)
urbanCyclist = Bicycle("Urban Cyclist", "hybrid", 6, 383)
cruiserClassy = Bicycle("Cruiser Classy", "casual", 12, 94)
ultimateArmstrong = Bicycle("Ultimate Armstrong", "racing", 8, 743)
happyHipster = Bicycle("Happy Hipster", "hybrid", 15, 325)

OffRampBikes = Shop("Off Ramp Bicycles", 1.20)
bikelist = [speedRacer, beachBum, urbanCyclist, cruiserClassy, ultimateArmstrong, happyHipster]
OffRampBikes.stock(bikelist)

Jenny = Customer("Jenny", 200)
Jenny.pricecheck(OffRampBikes)
Jenny.purchase(OffRampBikes)

Markus = Customer("Markus", 500)
Markus.pricecheck(OffRampBikes)
Markus.purchase(OffRampBikes)

Darla = Customer("Darla", 1000)
Darla.pricecheck(OffRampBikes)
Darla.purchase(OffRampBikes)
