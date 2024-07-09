# Kevin Sleem
# July 9, 2024
# P3HW2
# Employee Pay Calculations

#Request employee information
name = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

if hoursWorked > 40:
    #Calculate overtime
    ovtHours = hoursWorked - 40
    #Calculate overtime pay
    ovtPay = ovtHours * (payRate * 1.5)
    #Calculate paay for regular hours
    regPay = 40 * payRate
    #Calculate gross pay
    grossPay = regPay + ovtPay

else:
    #Set overtime hours and pay to zero
    ovtHours = 0
    ovtPay = 0
    regPay = payRate * hoursWorked
    grossPay = regPay

print("-"*37)
print("Employee name: ", name)
print('\n')
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<12} {"Gross Pay"}')
print('-'*80)


print(f'{hoursWorked:<15}{payRate:<12}{ovtHours:<12}${ovtPay:<14.2f}${regPay:<12.2f}${grossPay:.2f}')
