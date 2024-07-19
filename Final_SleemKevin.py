#Kevin Sleem
#July 20, 2024
#Final
#Grocery List Change Calculator

#function to show dictionary list
def show_avail_items():
    global grocery_list
    grocery_list = {'apples': 3.69, 'berries': 4.00, 'chocolate': 2.89,
                    'turkey': 6.99, 'cheese': 4.00, 'pepsi': 7.89,
                    'eggs': 3.50, 'bread': 3.00
                    }
    print(f'{"Grocery Item":<30} Price')
    print('-'*36)
    for key, value in grocery_list.items():
        print(f'{key:<30}${value:.2f}')
    return grocery_list
show_avail_items()

#function to add items to list
def grocery_checkout():
    global checkout_list
    checkout_list = []
    global grocery_list
    print('\n')
    print('*Welcome to the Grocery Checkout*')
    print('\n')
    item = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
    while item != 'end':
        if item in grocery_list:
            checkout_list.append(item)
            item = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
        elif item not in grocery_list:
            print('That item is not in stock')
            print('\n')
            item = input("Enter an item to add to the cart or type 'end' to stop adding items: ")

    return checkout_list
grocery_checkout()

#function to show checkout list
def show_cart():
    global checkout_list
    print('\n')
    print('The items currently in your cart are: ')
    for item in checkout_list:
        print(item)            
show_cart()

#function to calculate total owed
def calc_total(grocery_list, checkout_list):
    global total
    print('\n')
    print('Grocery Checkout Receipt')
    print('------------------------------')
    item_price_list = []
    for item in checkout_list:
        item_price = grocery_list[item]
        item_price_list.append(item_price)
        print(f'{item} {item_price:.2f}')
    subtotal = 0
    subtotal = sum(item_price_list)
    tax = subtotal * 0.02
    total = subtotal + tax
    print('\n')
    print(f'SUBTOTAL: {subtotal}')
    print('\n')
    print(f'{"TAX:":<20}${tax:.2f}')
    print(f'{"TOTAL:":<20}${total:.2f}')

calc_total(grocery_list, checkout_list)

#function to input cash
def cash_input():
    global change
    global total
    print('\n')
    print(f'You owe ${total:.2f} for the groceries')
    print('\n')
    cash = float(input('How much cash will you put in the self-checkout machine? '))
    print('\n')
    change = cash - total
    print(f'The change owed to you is ${change:.2f}')
    print('\n')
    print('Dispensing...')
    print('\n')
cash_input()

#function to disperse change
def disperse_change():
    #Convert change from a float to an integer
    global change
    change = float(f'{change:.2f}')
    change = int(change*100)

    if change == 0:
        print('No change')

    #Calculate the amount of each coin needed 
    num_dollars = change//100
    change = change - (num_dollars * 100)

    num_quarters = change//25
    change = change - (num_quarters * 25)

    num_dimes = change//10
    change = change - (num_dimes * 10)

    num_nickels = change//5
    change = change - (num_nickels * 5)

    num_pennies = change//1

    if num_dollars > 0:
        print(num_dollars, end=' ')
        if num_dollars == 1:
            print('Dollar')
        else:
            print('Dollars')

    if num_quarters > 0:
        print(num_quarters, end=' ')        
        if num_quarters == 1:
            print('Quarter')
        else:
            print('Quarters')

    if num_dimes > 0:
        print(num_dimes, end=' ')
        if num_dimes == 1:
            print('Dime')
        else:
            print('Dimes')

    if num_nickels > 0:
        print(num_nickels, end=' ')
        if num_nickels == 1:
            print('Nickel')
        else:
            print('Nickels')

    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1:
            print('Penny')
        else:
            print('Pennies')

disperse_change()
