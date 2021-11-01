# Entering the values for variables
a = int(input('First integral number = '))
b = int(input('Second integral number = '))
c = int(input('Third integral number = '))

# Calculating sum and product of numbers from 1 to c
summ = 0
prod = 1
for i in range(1, c + 1):
    summ += i
for i in range(1, c + 1):
    prod *= i

# Doing basic arithmetic operations inside print() function
# Displaying the results on screen/console
print(f'Addition: a + b = {a + b}')
print(f'Subtraction: a - b = {a - b}')
print(f'Multiplication: a * b = {a * b}')
print(f'Division: a / b = {a / b}')

# Displaying already calculated sum and product of numbers from 1 to c
print(f'Sum of numbers from 1 to {c} is {summ}')
print(f'Product of numbers from 1 to {c} is {prod}')

# Лотоцький Максим Павлович
