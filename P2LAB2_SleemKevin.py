# Kevin Sleem
# June 17, 2024
# P2LAB2
# Car Dictionary


#Create dictionary
cars = {"Camaro" : 18.21, "Prius" : 52.36, "Model S" : 110, "Silverado" : 26}
#Display values
keys = cars.keys()
values = cars.values()
print(keys)
print()
#Get input from user
car_input = input("Enter a vehicle to see it's mpg: ")
print()
#Get the mpg associated with the vehicle
mpg_output = cars[car_input]
print(f'The {car_input} gets {mpg_output} mpg.\n')
#Get the distance
distance =float(input(f'How many miles will you drive the {car_input}? '))
print()
#Calculate gallons of gas needed
gallons = distance / mpg_output
print(f'{gallons:.2f} gallons(s)of gas are needed to drive the {car_input} {distance} miles.')  
