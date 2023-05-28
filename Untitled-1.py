class Car:
"""A simple attempt to represent a car."""
u def __init__(self, make, model, year):
"""Initialize attributes to describe a car."""
self.make = make
Classes 163
self.model = model
self.year = year
v def get_descriptive_name(self):
"""Return a neatly formatted descriptive name."""
long_name = f"{self.year} {self.manufacturer} {self.model}"
return long_name.title()
w my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
class Car:
"""A simple attempt to represent a car."""
def __init__(self, make, model, year):
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0
def get_descriptive_name(self):
long_name = f"{self.year} {self.manufacturer} {self.model}"
return long_name.title()
def read_odometer(self):
print(f"This car has {self.odometer_reading} miles on it.")
def update_odometer(self, mileage):
if mileage >= self.odometer_reading:
self.odometer_reading = mileage
else:
print("You can't roll back an odometer!")
def increment_odometer(self, miles):
self.odometer_reading += miles
class Car:
--snip--
class ElectricCar(Car):
"""Represent aspects of a car, specific to electric vehicles."""
def __init__(self, make, model, year):
"""
Initialize attributes of the parent class.
Then initialize attributes specific to an electric car.
"""
super().__init__(make, model, year)
u self.battery_size = 75
v def describe_battery(self):
"""Print a statement describing the battery size."""
print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
class Car:
--snip--
class Battery:
--snip--
u def get_range(self):
"""Print a statement about the range this battery provides."""
if self.battery_size == 75:
range = 260
elif self.battery_size == 100:
range = 315
print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
--snip--
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
v my_tesla.battery.get_range()
class Car:
"""A simple attempt to represent a car."""
def __init__(self, make, model, year):
"""Initialize attributes to describe a car."""
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0
def get_descriptive_name(self):
"""Return a neatly formatted descriptive name."""
long_name = f"{self.year} {self.manufacturer} {self.model}"
return long_name.title()
def read_odometer(self):
"""Print a statement showing the car's mileage."""
print(f"This car has {self.odometer_reading} miles on it.")