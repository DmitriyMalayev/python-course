class Vehicle:  # blueprint for Objects representing vehicles
    def __init__(
        self, make, model
    ):  # initialized function used to set properties of the class
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("Tesla", "Model 3")

print(my_car.make)  # accessing property of the my_car instance
print(my_car.model)
my_car.get_make_model()  # method that is a function which is associated with the object.
my_car.moves()

your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


# Inheritance example
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # inherit from parent class
        self.faa_id = faa_id

    def moves(self):
        print("Flies along..")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along..")


class GolfCart(Vehicle):
    pass  # inherit everything as is


print("")
print("")

cessna = Airplane("Cessna", "Skyhawk", "N-12345")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")


# Polymorphism example using a list of objects
# The ability to behave differently in response to different input messages
# They all have a 'get_make_model' and a'moves' method but they have different responses to these methods
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
