# Task 1
# Напишіть функцію, яка поверне максимальне значення зі списку чисел.
def maxx(arr):
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    return result


list1 = [1, 2, 3, 66, 57, -40]
print(maxx(list1))

# Task 2
# Реалізуйте функцію, параметрами якої є - два числа і рядок. Повертає вона конкатенацію рядки з сумою чисел.
def func(x, y, text):
    return text + str(x + y)


a, b, line = 4, 9, "String"
print(func(a, b, line))

# Task 3
# Реалізуйте функцію, що виводить на екран прямокутник з зірочок «*». Її параметрами будуть цілі числа,
# які описують довжину і ширину такого прямокутника.

def rectangle_filled(length, width):
    if (length or width) <= 0:
        print("No such possible rectangle")
    else:
        for i in range(length):
            print("*" * width)

def rectangle_empty(length, width):
    if (length or width) <= 0:
        print("No such possible rectangle")
    else:
        for i in range(length):
            print(("*" * width) if i == 0 or i == length-1 else "*" + (" " * (width-2)) + ("*" if width > 1 else ""))


print('Filled rectangle:')
rectangle_filled(5, 5)
print('Empty rectangle:')
rectangle_empty(5, 5)
print('Filled rectangle:')
rectangle_filled(5, 1)
print('Empty rectangle:')
rectangle_empty(5, 1)

# Task 4
# Напишіть функцію, яка реалізує лінійний пошук елемента в списку цілих чисел. Якщо такий елемент в списку є,
# то поверніть його індекс, якщо немає, то поверніть число «-1».

def linear_search(element, arr):
    for i in range(len(arr)):
        if element == arr[i]:
            return i
    return -1


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [3, 4, 5, 6, 7]
print(linear_search(3, list1))
print(linear_search(3, list2))

# Task 5
# Напишіть функцію, яка поверне кількість слів у рядку тексту.
import string

def wordss(line):
    not_letters = string.digits + string.punctuation
    words_count = 0
    for i in line.split():
        for u in i:
            if u not in not_letters:
                words_count += 1
                break

    return words_count


line1 = "Напишіть функцію, яка поверне кількість слів у рядку тексту."
line2 = "Напишіть функцію, яка реалізує лінійний пошук елемента в списку цілих чисел."
line3 = "      "
line4 = ",,,... .,,..,. .,   "
print(f'{wordss(line1)}, {wordss(line2)}, {wordss(line3)}, {wordss(line4)}.')
