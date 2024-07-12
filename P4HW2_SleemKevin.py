# Kevin Sleem
# July 12, 2024
# P4HW2
# Employee Pay Calculations

#Initialize variables for totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0
overtime_hours = 0

#Main loop to enter employee data
while True:
    #Enter Employee Name or Done; if done, print out summary
    employee_name = input("Enter employee's name or ""Done"" to terminate: ")
    if employee_name == 'Done':
        print(f'Total number of employees entered: {total_employees}')
        print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
        print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
        print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
        break
    
    #Finish data input with hours worked and payrate
    hours_worked = float(input("Enter number of hours worked: "))
    payrate = float(input("Enter employee's pay rate: "))
    #Print employee name
    print("------------------------------")
    print("Employee name:", employee_name)
    print('\n')
    print("Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay")
    print('-----------------------------------------------------------------------')

    #Calculate regular pay and overtime pay for gross pay
    overtime = hours_worked - 40
    regular_hours = hours_worked - overtime

    if hours_worked <= 40:
        overtime = 0.0

    overtime_pay = overtime * payrate * 1.5
    regular_pay = regular_hours * payrate
    gross_pay = regular_pay + overtime_pay

    #Update totals
    total_employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    #Format decimals
    payrate = (f'{payrate:.2f}')
    overtime = (f'{overtime:.2f}')
    overtime_pay = (f'{overtime_pay:.2f}')
    regular_pay = (f'{regular_pay:.2f}')
    gross_pay = (f'{gross_pay:.2f}')

    print(f'{hours_worked:.2f} {payrate:>13} {overtime:>8} {overtime_pay:>10} {regular_pay:>14} {gross_pay:>12}')


    


