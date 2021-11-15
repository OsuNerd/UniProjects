# Написати програму, яка зчитує 4 числа з клавіатури і виводить на екран найбільше з них.
print("Input 4 numbers: ")
k = []
for q in range(1, 5):
    k.append(float(input(f'{q}: ')))
p = [0, 0, 0, 0]
for i, g in zip(k, range(0, 4)):
    for h in k:
        if i >= h:
            p[g] += 1
for i in range(0,4):
    if p[i] == 4:
        print(f'Yout largest number is: {k[i]}')
        break
# Other way
a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))
d = float(input("4: "))
if a >= b and a >= c and a >= d:
    print(f'Yout largest number is: {a}')
elif b >= a and b >= c and b >= d:
    print(f'Yout largest number is: {b}')
elif c >= a and c >= b and c >= d:
    print(f'Yout largest number is: {c}')
elif d >= a and d >= b and d >= c:
    print(f'Yout largest number is: {d}')

# Визначити кількість днів в році, який вводить користувач. У високосному році - 366 днів, тоді як в звичайному їх 365.
year = int(input("Please, input a year that you want to know about: "))
if year % 400 == 0:
    print("This year is a leap year and it has 366 days.")
elif year % 100 == 0:
    print("This year is a regular year and it has 365 days.")
elif year % 4 == 0:
    print("This year is a leap year and it has 366 days.")
else:
    print("This year is a regular year and it has 365 days.")

# Трикутник існує тільки тоді, коли сума будь-яких двох його сторін більше третьою. Дано: a, b, c - сторони
# передбачуваного трикутника. Напишіть програму, яка вкаже, чи існує такий трикутник чи ні.
a, b, c = float(input("Enter value for the first side a: ")), \
          float(input("Enter value for the second side b: ")), \
          float(input("Enter value for the third side c: "))
if a < b + c and b < a + c and c < a + b:
    print("Yes, this triangle can exist.")
else:
    print("No, this triangle can't exist.")

# Виведіть на екран всі числа в діапазоні від 1 до 100 кратні 7.
for i in range(0, 101):
    if i % 7 == 0:
        print(i, end=" ")
print()
# second way
for i in range(0, 101, 7):
    print(i, end=" ")
print()

# Обчислити за допомогою циклу факторіал числа n
n = int(input("Input some natural number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f'Factorial of your number: {factorial}')

# Виведіть на екран «пісочний годинник», максимальна ширина яких зчитується з клавіатури (число непарне).
# У прикладі ширина дорівнює 5.
width = int(input("Enter width of the hourglass (odd number, not zero): "))
while width % 2 == 0 or width <= 0:
    width = int(input("Invalid number. Please, enter correct width of the hourglass (odd number, not zero): "))
for i in range(0, width):
    print(("*" * (width - 2 * i) if i * 2 <= width else "*" * (-1 * (width - (i + 1) * 2))).center(width, " "))

# За допомогою циклів вивести на екран всі прості числа від 1 до 100.
counter = 100
number = 1
while counter > 0:
    counter = counter - 1
    print(number, end=" ")
    number += 1
print()
# or
for i in range(1, 101):
    print(i, end=" ")
print()
