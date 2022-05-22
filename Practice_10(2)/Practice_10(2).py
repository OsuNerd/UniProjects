# Task 1
# Напишіть функцію аddRightDigit (d, k), яка повинна додавати до цілого позитивного числа K справа цифру D
# (D - цілочисельне значення в діапазоні 0-9, К - цілочисельне значення).
def addRightDigit(d,k):
    k = str(k) + str(d)
    return k

print(addRightDigit(5,100)) # prints 1005

# Task 2
# Напишіть функцію, яка приймає два цілих числа n і k і повертає число, що містить k перших цифр числа n.
def func(n,k):
    if k > 0:
        if k < len(str(n)):
            return n//(10**((len(str(n)))-k)) # return first k digits of n
        else:
            return n # return n if k > or == to the number of digits in n
    else:
        return None # return None if k is negative or == 0

number, k = 12345678910, 4

print(f'My number:       {number}')
print(f'Function result: {func(number,k)}')
