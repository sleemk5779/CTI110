#Kevin Sleem
#June 20, 2024
#P1HW2
#This lab includes input and print functions to create a travel itinerary and
#budget

print('This program calculates and displays travel expenses')
print('\n')

budget = int(input('Enter Budget: '))
travel_destination = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
hotel = int(input('Approximately how much will you need for accomodation/hotel? '))
food = int(input('Last, how much do you need for food? '))

print('\n')
print('--------Travel Expenses--------')
print('Location:', travel_destination)
print('Initial Budget:', budget)
print('\n')
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print('\n')
print('Remaining Balance:', budget - gas - hotel - food)
