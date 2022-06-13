class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# First instantiation of the class Location
loc1 = Location("Tomas", "Portugal")

# Call a method from the instantiated class
loc1.myLocation()

loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")

loc2.myLocation()
loc3.myLocation()
your_loc = Location("Dan", "Spain")
your_loc.myLocation()
