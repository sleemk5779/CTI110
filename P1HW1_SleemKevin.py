#Kevin Sleem
#June 20, 2024
#P1HW1
#This lab includes input and print functions to create math functions

print('----Calculating Exponents----')
print('\n')

base_value = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent: '))
print('\n')

first_calculation = base_value**exponent
print(base_value, 'raised to the power of', exponent, 'is', first_calculation, '!!')
print('\n')

print('----Addition and Subtraction----')
print('\n')

starting_integer = int(input('Enter a starting integer: '))
add_integer = int(input('Enter an integer to add: '))
subtract_integer = int(input('Enter an integer to subtract: '))
print('\n')

second_calculation = starting_integer + add_integer - subtract_integer
print(starting_integer, '+', add_integer, '-', subtract_integer, 'is equal to', second_calculation)
