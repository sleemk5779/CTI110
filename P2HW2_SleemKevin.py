#Kevin Sleem
#June 28, 2024
#P2HW2
#Grade Calculator

#Enter grades for module 1 through 6
module_1 = float(input('Enter grade for Module 1: '))
module_2 = float(input('Enter grade for Moduel 2: '))
module_3 = float(input('Enter grade for Module 3: '))
module_4 = float(input('Enter grade for Module 4: '))
module_5 = float(input('Enter grade for Module 5: '))
module_6 = float(input('Enter grade for Module 6: '))

#Skip a line
print('\n')
print('------------Results------------')
#Create list storing grades from module 1 through 6
grades = [module_1, module_2, module_3, module_4, module_5, module_6]
#print lowest grade using list function min
print(f'{"Lowest Grade:":<20} {min(grades)}')
#print highest grade using list function max
print(f'{"Highest Grade:":<20} {max(grades)}')
#print sum of grades using list function sum
print(f'{"Sum of Grades:":<20} {sum(grades)}')
#create assignment for average of grades
average = sum(grades) / len(grades)
#print average
print(f'{"Average:":<20} {average:.2f}')
print('--------------------------------------')
