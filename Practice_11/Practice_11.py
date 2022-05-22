# Make both iteration and recursion versions of algorithms
import time
import numpy as np
import random
# Task 1
# Сформувати функцію, що буде обчислювати факторіал заданого користувачем натурального числа n.

def FactorialRecur(n):
    if n < 1:
        if n == 0:
            return 1
        else:
            print("Error, number lower than 0 can't be integrated.")
            return None
    else:
        return n * FactorialRecur(n-1)

def FactorialIter(n):
    if n < 0:
        print("Error, number lower than 0 can't be integrated.")
        return None
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = 990
print(f'My number - {number}\nRecursive factorial - {FactorialRecur(number)}\n'
      f'Iterative factorial - {FactorialIter(number)}')
time1 = time.perf_counter()
FactorialRecur(number)
time2 = time.perf_counter()
print(f'Recursive execution time: {time2-time1:0.10f}')
time1 = time.perf_counter()
FactorialIter(number)
time2 = time.perf_counter()
print(f'Iterative execution time: {time2-time1:0.10f}')

# Обидва алгоритми є нескладними для сприйняття.
# Рекурсивний алгоритм робить як мінімум одне порівняння за цикл, а ітеративний робить лише одне у початку.
# Рекурсивна функція займає значно більше місця у стеку, ніж змінна result у ітеративній.
# Загалом, якщо опиратися на час який видає програма, ітераційний спосіб є швидшим.
# Робимо висновок, що краще використовувати ітераційну функцію, хоча різниця не є занадто великою, якщо враховувати
# рідку потребу у вичесленні дуже великих факторіалів (рекурсивний довше на ~50%).

# Task 2
# Сформувати функцію для обчислення цифрового кореню натурального числа. Цифровий корінь отримується наступним чином:
# необхідно скласти всі цифри заданого числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір,
# поки сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого числа.
def DigRootRecur(n):
    if n < 10:
        return n
    else:
        return DigRootRecur(RecurSum(n))

def RecurSum(n):
    if n < 10:
        return n
    else:
        return n % 10 + RecurSum(n // 10)


def DigRootIter(n):
    while n >= 10:
        stage = 0
        for i in str(n):
            stage += int(i)
        n = stage
    return n


number = 43254253653750439278594327598430275439826438920574389256432059826354325783456923465
print(f'My number - {number}\n Recursive digital root - {DigRootRecur(number)}\n'
      f'Iterativ digital root - {DigRootIter(number)}')
time1 = time.perf_counter()
DigRootRecur(number)
time2 = time.perf_counter()
print(f'Recursive execution time: {time2-time1:0.10f}')
time1 = time.perf_counter()
DigRootIter(number)
time2 = time.perf_counter()
print(f'Iterative execution time: {time2-time1:0.10f}')

# Обидві функції є відносно зрозумілими, на мій погляд ітерційний алгоритм є ліпшим у реалізації.
# Змінні ітераційного способу все ще займають менше пам'яті, ніж стек рекурсивного.
# За результатами більш швидким є ітераційний спосіб. Для цієї задачі краще використовувати ітерацію, але різниця незначна
# (Рекурсивний довше на ~23%).

# Task 3
# Сформувати функцію для обчислення індексу максимального елементу масиву n*n, де 1<=n<=5.
def MatrixMaxRecur(m, row, column, Max = (0,0)):
    if m[row, column] > m[Max]:
        Max = (row, column)
    if column != 0:
        column -= 1
        return MatrixMaxRecur(m, row, column, Max)
    elif row != 0:
        row -= 1
        column = m.shape[1]-1
        return MatrixMaxRecur(m, row, column, Max)
    else:
        return Max


def MatrixMaxIter(m):
    row, column = m.shape[0] - 1, m.shape[1] - 1
    Max = [-101, (0,0)]
    while row >= 0:
        while column >= 0:
            if m[row, column] > m[Max[1]]:
                Max = [m[row, column], (row, column)]
            column -= 1
        row -= 1
        column = m.shape[1] - 1
    return Max


matrix = np.random.randint(-100,100,(random.randint(1,5),random.randint(1,5)))
# matrix = np.array([[ 50, -51, 75],[78,  88, 59],[66, 85, 444]])
r, c = matrix.shape
print(f'My matrix: \n{matrix}')

time1 = time.perf_counter()
result1 = MatrixMaxRecur(matrix,r-1,c-1)
time2 = time.perf_counter()
print(f'Largest number - {matrix[result1]}, its index - {result1}')
print(f'Recursive execution time: {time2-time1:0.10f}')
time1 = time.perf_counter()
result2 = MatrixMaxIter(matrix)
time2 = time.perf_counter()
print(f'Largest number - {result2[0]}, its index - {result2[1]}')
print(f'Iterative execution time: {time2-time1:0.10f}')

# Зазвичай ітераційний спосіб трохи швидший за рекурсивний. Головною перевагою ітераційного способу тут є потреба у
# невеликому обсягу пам'яті, коли як рекурсивний має достатньо великий стек. Також, при більших матрицях, можливе
# досягнення ліміту на рекурсії функції. На мій погляд ітераційний спосіб є трохи зрозумілішим, ніж рекурсивний.
# Ітераційний спосіб не потребує вводу інших даних окрім самої матриці.
# Напевно можлива оптимізація обох функцій і після цього висновки можуть змінитися.
