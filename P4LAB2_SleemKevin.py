#Kevin Sleem
#July 11, 2024
#P4LAB2
#Number Mulitplier

#Use while to control the program
keep_going = "yes"
while keep_going.lower() == "yes":
    #for loop goes here
    num = int(input("Enter an integer: "))
    print("\n")

    if num >= 0:
        for i in range(1, 12+1):
            print(f'{num} + {i} = {num * i}')
        print("\n")
    else:
        print("This program does not handle negative numbers.")
        print('\n')

    keep_going = input("Would you like to run the program again? Enter yes or no: ")
    
#Input, press enter key to exit
print('The program has ended')

