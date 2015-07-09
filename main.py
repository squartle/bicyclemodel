import bicycles.py

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
