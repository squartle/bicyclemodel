
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

    def stock(self, list):
        for i in list:
            price = self.markup * i.prod_cost
            self.inventory[i] = round(price, -1)

    def sell(self, i):
        self.profits += self.inventory[i] - i.prod_cost
        del self.inventory[i]
        print "This is what we have left in stock: %s." % self.inventory

class Customer(object):
    def __init__(self, funds):
        self.funds = funds
        self.ownership = []
        self.affordable = []

    def pricecheck(self, Shop):
        for i in Shop.inventory:
            if self.funds >= Shop.inventory[i]:
                self.affordable.append(i)
                print "%s is right in the range I'm looking for." % i
            else:
                print "I can't afford %s!" % i

    def purchase(self, Shop):
        import random
        chosen = random.choice(self.affordable)
        self.ownership.append(chosen)
        self.funds -= Shop.inventory[chosen]
        Shop.sell(chosen)
        print "I have $%s leftover and I just bought %s. " %(self.funds, chosen)

speedRacer = Bicycle("racing", 12, 220)
beachBum = Bicycle("casual", 34, 129)
urbanCyclist = Bicycle("hybrid", 6, 383)
cruiserClassy = Bicycle("casual", 12, 94)
ultimateArmstrong = Bicycle("racing", 8, 743)
happyHipster = Bicycle("hybrid", 15, 325)

OffRampBikes = Shop("Off Ramp Bicycles", 1.20)
bikelist = [speedRacer, beachBum, urbanCyclist, cruiserClassy, ultimateArmstrong, happyHipster]
OffRampBikes.stock(bikelist)
print OffRampBikes.inventory

Jenny = Customer(200)
Jenny.pricecheck(OffRampBikes)
Jenny.purchase(OffRampBikes)
