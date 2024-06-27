# Kevin Sleem
# June 27, 2024
# P2HW1
# Travel Itinerary

print("This program calculates and displays travel expenses\n")

# Request information

budget = float(input("Enter Budget: "))
print()

location = input("Enter your travel destination: ")

print()
fuel = float(input("How much do you think you will spend on gas? "))

print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))

# add expenses

expenses = fuel + hotel + food

remainAmount = budget - expenses

# display results

print(12 * "-","Travel Expenses", 12 * "-")
print(location)
print(budget)
print(fuel)
print(hotel)
print(food)
print("----------------------------------------\n")
print(remainAmount)




