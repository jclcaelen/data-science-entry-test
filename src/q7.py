class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    # Example of creating new classes, and the structure:
    # https://stackoverflow.com/questions/8609153/why-do-we-use-init-in-python-classes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print("f{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

new_car = Car("Toyota", "Corolla", 2020)
new_car.describe_car()
