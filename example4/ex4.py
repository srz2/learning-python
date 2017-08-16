cars = 100
carCapacity = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
cars_driven = drivers
carCapacity = cars_driven * carCapacity
avgPassengerPerCar = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", carsNotDriven, "empty cars today."
print "We can transport", carCapacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", avgPassengerPerCar, "in each car."
