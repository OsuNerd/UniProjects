import time
# Для кожної з задач алгоритм реалізувати з використанням рекурсії і ітерації.
# Task 1
# Сформувати функцію для введення з клавіатури послідовності чисел і виведення її на екран у зворотному порядку
# (завершаючий символ послідовності – крапка)

def list_iter():
    arr = []
    while True:
        x = input('Please, enter a single number you want to add to your list. When you\'re done, enter a ".": ')
        # Checking if the input is a float or an integral value with try/except method
        try:
            x = float(x)
            int(x)
            # Adding elements based on their type
            if x % 1 == 0:
                arr.append(int(x))
            else:
                arr.append(float(x))
        except ValueError:
            if x == ".":
                # Reversing the array
                arr = arr[::-1]
                return print(arr)
            else:
                print("Enter a valid number or a \".\" to end the function.")

def list_recur(arr=None):
    if arr is None:
        arr = []
    x = input('Please, enter a single number you want to add to your list. When you\'re done, enter a ".": ')
    # Checking if the input is a float or an integral value with try/except method
    try:
        x = float(x)
        int(x)
        # Adding elements based on their type
        if x % 1 == 0:
            arr.append(int(x))
            return list_recur(arr)
        else:
            arr.append(float(x))
            return list_recur(arr)
    except ValueError:
        if x == ".":
            # Reversing the array
            arr = arr[::-1]
            return print(arr)
        else:
            print("Enter a valid number or a \".\" to end the function.")
            return list_recur(arr)


list_iter()
list_recur()

# IMPORTANT
# Because functions wait for user input, it's impossible to time them correctly in their current state.
# Functions also contain input checking that slows down their work.
# Using iteration function is a little more straight forward and should take less space because of lack of stack.
# In their current form, using either one seems fine.
# ВАЖЛИВО
# Через те, що функція чекає на ввід чисел від користувача, стає неможливим правильно виміряти час їх виконання.
# Також функції перевіряють корректність вводу, що звичайно затримує їх.
# Використання ітераційної функції здалося мені легчим та має займати менше місця через відсутність стеку.
# У даному вигляді, на мою думку, використовувати можна будь-яку з них.

# Task 2
# Сформувати функцію, що визначатиме чи є задане натуральне число простим. Простим називається число, що більше за
# 1 та не має інших дільників, окрім 1 та самого себе.

def prime_iter(x: int):
    if x > 1:
        for u in range(2, int(x)):
            if int(x) % u == 0:
                return False  # In case of a number not being prime, return False
        return True  # If function doesn't end, meaning no divisible cases, the number is prime, returns True
    return False

def prime_recur(x: int, y=2):
    if x <= 2:
        return True if x == 2 else False
    if y == x:
        return True
    else:
        if x % y == 0:
            return False
        else:
            return prime_recur(x, y+1)


test_numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
print("\nTask 2\nChecking if the numbers are prime\n")
print(f'Numbers to check: {test_numbers}')

for i in test_numbers:
    print(f'Is number {i} prime? Iteration result: {prime_iter(i)} Recursion result: {prime_recur(i)}')
itime1 = time.perf_counter_ns()
for i in test_numbers:
    prime_iter(i)
itime2 = time.perf_counter_ns()
rtime1 = time.perf_counter_ns()
for i in test_numbers:
    prime_iter(i)
rtime2 = time.perf_counter_ns()

print(f'It takes {itime2-itime1}ns for iteration function, and {rtime2-rtime1}ns for recursion function '
      f'to test {len(test_numbers)} numbers.')

# Recursion function usually takes less time, although probably takes a little bit more space because of stack.
# Personally, recursive function seems a little harder to develop, although it's not nearly hard enough to not use it.
# Overall, recursive function seems like a better way to go about finding prime numbers.
# Рекурсивна функція займає трішки менше часу, хоча при цьому напевной займає трохи більше пам'яті через стек.
# Для мене, написати рекурсійну функцію було важче за ітеративну, але точно не настільки, щоб не користуватися нею.
# Загалом, для знаходження простих чисел, здається, краще використовувати рекурсивну функцію.


# Task 3
# Сформувати функцію для переведення натурального числа з десяткової системи числення у шістнадцятирічну.

test_numbers_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 33, 48, 64, 65, 999]

def convert_10to16_recur(x):
    helping_string = "0123456789ABCDEF"
    r = int(x % 16)
    if x - r == 0:
        return helping_string[r]
    return convert_10to16_recur((x-r) / 16) + helping_string[r]

def convert_10to16_iter(x):
    helping_string = "0123456789ABCDEF"
    result = ""
    while True:
        r = int(x % 16)
        if x - r == 0:
            return helping_string[r] + result
        x = (x - r) / 16
        result = helping_string[r] + result


print("\nTask 3\nConverting numbers\n")
print(f'Numbers to convert: {test_numbers_2}')
for i in test_numbers_2:
    print(f'Number {i:>5}. Iterative results: {convert_10to16_iter(i):>5}. '
          f'Recursive results: {convert_10to16_recur(i):>5}. '
          f'Built-in function results: {hex(i):>7}')

itime1 = time.perf_counter_ns()
for i in test_numbers_2:
    convert_10to16_iter(i)
itime2 = time.perf_counter_ns()
rtime1 = time.perf_counter_ns()
for i in test_numbers_2:
    convert_10to16_recur(i)
rtime2 = time.perf_counter_ns()
print(f'It takes {itime2-itime1}ns for iteration function, and {rtime2-rtime1}ns for recursion function '
      f'to convert {len(test_numbers_2)} numbers.')

# Once again, recursion function seems to be a bit faster, but takes a little more space because of stack.
# However, this time I found it way easier to and shorter to make a recursion function rather than iteration one.
# In conclusion, it's better to use recursion function to convert numbers from base10 to base16.
# Знову ж таки, рекурсія є трохи швидша за ітеративний спосіб, але має займати трохи більше місця через стек.
# Хоча у цьому випадку, створити рекурсійну функцію було значно легче ніж ітераційну, та вона займає меньше місця.
# Тобто, для переведення з десяткової системи числення у шістнадцятирічну, краще використовувати рекурсію.
