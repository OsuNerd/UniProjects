# First Task: Write a Python program using loop structure to print numbers 1.2.3……9
for i in range(1, 9+1):
    if i < 9:
        print(i, end=".")
    else:
        print(i)

# Second Task: Write a Python program using loop structure to print numbers 9.8.7…..1
a = ""
for i in range(1, 9+1):
    if i > 8:
        a = f'{i}' + a
    else:
        a = f'.{i}' + a
print(a)

# Third Task: Write a Python program to print on the screen odd numbers between 5..13
for i in range(5, 13+1, 2):
    print(i, end=" ")
print()
# Third Task v.2
for i in range(5, 13+1):
    if i % 2 != 0:
        print(i, end=" ")
print()

# Fourth Task: Write a Python program to add all the numbers entered by a user until user enters 0.
print("Input numbers and then 0 to calculate their sum")
number = float(input("Number: "))
number_sum = 0
while number != 0:
    number_sum += number
    number = float(input("Another Number: "))
print(f'Your sum of numbers: {number_sum}')

# Fifth Task: Write a Python Program to reverse a number. For example, if user enters 123 as input
# then 321 is printed as output.
b = str(input("Input a number you want to reverse: "))
c = ""
for i in b:
    c = f'{i}' + c
print(c)
# Fifth Task v.2
d = int(input("Input a natural number you want to reverse: "))
e = d
counter = 0
reversed_number = ""
while e >= 1:
    counter += 1
    e = e / 10
for i in range(1, counter+1):
    reversed_number = str(d // (10 ** (counter - i)) % 10) + reversed_number
print(reversed_number)

# Sixth Task: Write Python program to find and print factorial of a number
num = int(input("Input a number: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f'Factorial of a number: {factorial}')
