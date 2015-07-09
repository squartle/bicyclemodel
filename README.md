# bicyclemodel
lesson 1.3.4

____
main.py imports bicycles.py, bicyclemodel.py is "all together" (not sure what the technical term is here... unfactored?).  My machine has Python 3 installed and I was having some trouble getting python 2 and everything was broken and that's the only way I could test it.
____

I didn't really do the extra challenge or the extension.  Classes had me totally stumped for this whole week, so I stuck to the basics... but I'm pretty sure I understand the extension in the abstract.

class Wheel(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost

class Frame(object):
  def __init__(self, material, weight, cost):
    self.material = material
    self.weight = weight
    # theoretically I could create a dictionary (data frame?) of various materials/weights and have it identify the material and pull the weight... thus opening up the possibility to do frames with different sizes, like size_medium = 1.5 * materialdict[weight]; materialdict[] would have to be top level (could also add wheel/tire materials)
    self.cost = cost

class Bicycle(object):
  def __init__(self, name, wheel, frame):
    self.name = name
    self.wheel = wheel
    self.frame = frame
    self.weight = (wheel.weight * 2) + frame.weight
    self.prod_cost = (wheel.prod_cost * 2) + frame.prod_cost
    
A bicycle manufacturer class would function almost identically to an actual store.  You could go balls deep and have different manufacturers for wheels, etc. and set prices and markups for each manufacturer... yeah, manufacturer is nbd.  Basically adds a layer of a class almost excelt like Shop(object).


