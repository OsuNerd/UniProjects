# Task 1
# 1. Дан масив цілих чисел. Кількість елементів запросити з клавіатури. Знайти:
# максимальний елемент масиву і його номер;
# мінімальний елемент масиву.

import random

# Створюємо масив з випадковими числами, кількість яких визначає користувач
numbers = []
x = int(input("Please, enter the amount of numbers in an array: "))
for i in range(x):
    numbers.append(random.randint(0,100))

# Знаходимо максимальне число у масиві та його порядковий номер; мінімальний номер
print(*numbers, sep = ", ") # Вивід масиву на екран
# Перший спосіб
maximum, minimum, counter = numbers[0], numbers[0], 0
for u, i in zip(range(1,len(numbers)+1), numbers):
    if i > maximum:
        maximum = i
        counter = u
    if i < minimum:
        minimum = i
print(f'Максимальне число у масиві - {maximum}, його порядковий номер - {counter}, його індекс - {counter-1}')
print(f'Мінімальне число в масиві: {minimum}')
# Другий спосіб
print(f'Максимальне число у масиві - {max(numbers)}, його порядковий номер - {numbers.index(max(numbers)) + 1}'
      f', його індекс - {numbers.index(max(numbers))}')
print(f'Мінімальне число в масиві: {min(numbers)}')

# Task 2
# 2. Дан масив з 10 елементів. Перші 4 впорядкувати по зростанню, останні 4 по спадаючій.
numbers2 = []
for i in range(10):
    numbers2.append(random.randint(0,99))
print(f'До сортування: {str(numbers2)[1:-1]}')

def sorti(array,amount=None,side="l",way=1): # (numbers2,4,l,1) and (numbers2,4,r,-1) where 1 and -1 are rising and descending
    # таблиця значень
    # (numbers2,4,l,1)  array[0:3:1] range(0,3,1)
    # (numbers2,4,l,-1) array[0:3:1] range(0,3,1)
    # (numbers2,4,r,-1) array[6:9:1] range(6,9,1)
    # (numbers2,4,r,1)  array[6:9:1] range(6,9,1)
    if side == "l": x = 0
    else: x = 1
    if amount == None: amount = len(array)
    while True:
        counter = 0
        for i, u in zip(array[0+(len(array)-amount)*x:amount-1+(len(array)-amount)*x:1],
                        range(0+(len(array)-amount)*x,amount-1+(len(array)-amount)*x,1)):
            if way*i > way*array[u + 1]:
                array[u], array[u + 1] = array[u + 1], array[u]
                counter = 1
        if counter == 0:
            return array
numbers2 = sorti(sorti(numbers2,4,"r",-1),4,"l",1)
print("Після сортування:", str(numbers2)[1:-1])
# Додатковий тест функції: 3 числа зліва в порядку спадання, 7 чисел справа в порядку збільшення
numbers2 = sorti(sorti(numbers2,3,"l",-1),7,"r",1)
print("Після сортування:", str(numbers2)[1:-1])

# Task 3
# 3. Дан масив 20 цілих чисел на відрізку [-2; 5]. Впорядкувати масив, видаливши нулі із зсувом вліво.
array = []
for i in range(20):
    array.append(random.randint(-2,5))
print(f'До сортування: {str(array)[1:-1]}')
array = sorti(array)
print(f'Після сортування: {str(array)[1:-1]}')
if 0 in array:
    l,r = array.index(0), abs(len(array)-array[::-1].index(0))
    array = array[0:l] + array[r:len(array)]
print(f'Після видалення нулів: {str(array)[1:-1]}')
