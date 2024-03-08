"""
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих транспортные средства:
"""


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class Motorcycle(LandVehicle):
    pass


class Bicycle(LandVehicle):
    pass


class Propeller(AirVehicle):
    pass


class Jet(AirVehicle):
    pass


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(LandVehicle, Vehicle))
print(issubclass(WaterVehicle, Vehicle))
print(issubclass(AirVehicle, Vehicle))

# TEST_2:
print("\nтест 2")
print(issubclass(Car, LandVehicle))
print(issubclass(Motorcycle, LandVehicle))
print(issubclass(Bicycle, LandVehicle))

# TEST_3:
print("\nтест 3")
print(issubclass(Propeller, AirVehicle))
print(issubclass(Jet, AirVehicle))

# TEST_4:
print("\nтест 4")
print(issubclass(Car, Vehicle))
print(issubclass(Motorcycle, Vehicle))
print(issubclass(Bicycle, Vehicle))
print(issubclass(Propeller, AirVehicle))
print(issubclass(Jet, AirVehicle))

# TEST_5:
print("\nтест 5")
print(issubclass(Car, WaterVehicle))
print(issubclass(Motorcycle, WaterVehicle))
print(issubclass(Bicycle, WaterVehicle))

print(issubclass(Car, AirVehicle))
print(issubclass(Motorcycle, AirVehicle))
print(issubclass(Bicycle, AirVehicle))

# TEST_6:
print("\nтест 6")
print(issubclass(Propeller, LandVehicle))
print(issubclass(Jet, LandVehicle))

print(issubclass(Propeller, WaterVehicle))
print(issubclass(Jet, WaterVehicle))
