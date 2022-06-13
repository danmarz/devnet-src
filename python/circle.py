# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2 * radius
class Circle:
  def __init__(self, radius):
    self.radius = radius
  def circumference(self):
    pi = 3.14
    circumferenceValue = pi * self.radius * 2
    return circumferenceValue
  def printCircumference(self):
    myCircumference = self.circumference()
    print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

# First instantiation of the Circle class.
circle1 = Circle(2)

# Call the printCircumference for the instantiated circle1 class.
circle1.printCircumference()

# Two more instantiations and method calls for the Circle class.
circle2 = Circle(5)
circle2.printCircumference()
circle3 = Circle(7)
circle3.printCircumference()

