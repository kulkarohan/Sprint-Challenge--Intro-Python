# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Vehicle is the base class
class Vehicle:
    pass

# GroundVehicle is a Vehicle
class GroundVehicle(Vehicle):
    pass

# Car is a GroundVehicle
class Car(GroundVehicle):
    pass

# Motorcycle is a GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# FlightVehicle is a Vehicle
class FlightVehicle(Vehicle):
    pass

# Airplane is a FlightVehicle
class Airplane(FlightVehicle):
    pass

# Starship is a FlightVehicle
class Starship(FlightVehicle):
    pass
