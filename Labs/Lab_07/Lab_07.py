import numpy as np
# Task 1
# Напишіть програму, що виводить на екран елементи лінійного масиву (елементи масиву задаються користувачем)
# у зворотному порядку
# 10 20 30 40 55 66 77 88 99 111

arr = np.array(input("Enter elements to an array dividing them by space: ").split(" "))
print(arr[::-1])

# Task 2
# Напишіть програму, що виводить на екран транспоновану матрицю 3*3 (початкова матриця задається користувачем)
arr = np.array([input("Enter 3 elements to " + str(i) + " row of matrix, dividing them by space: ").split(" ") for i in
                range(1, 4)])
print(f'Your matrix: \n{arr}')
# Using numpy .transpose()
print(f'Your matrix after transposing: \n{arr.transpose()}')
# Other way
temp = []
for i in arr:
    for u in i:
        temp.append(u)
transposed = []
for i in range(len(arr[0])):
    transposed.append([])
    for u in range(len(arr)):
        transposed[i].append(temp[i+u*len(arr[0])])
transposed = np.array(transposed)
print(f'Your matrix after transposing: \n{transposed}')

# Task 3
# Напишіть програму, що визначає добуток двох квадратних матриць 3*3 (необхідно враховувати розмірність).
# Результати множення елементів занесіть до нової матриці та виведіть її на екран
arr1 = np.random.randint(-10, 10, (3, 3))
arr2 = np.random.randint(-10, 10, (3, 3))
print(f'First matrix:\n{arr1}\nSecond matrix:\n{arr2}')
# Using numpy functions
# 1 way. Corresponding elements
arr3 = arr1 * arr2
print(f'Multiplied corresponding elements:\n{arr3}')
# 2 way. Mathematical multiplying
arr3 = np.matmul(arr1, arr2)
print(f'Multiplied matrices:\n{arr3}')
# Without numpy functions
# 1 way. Corresponding elements
arr3 = np.zeros((3, 3), int)
for i in range(len(arr1)):
    for u in range(len(arr1)):
        arr3[i, u] = arr1[i, u]*arr2[i, u]
print(f'Multiplied corresponding elements:\n{arr3}')
# 2 way. Mathematical multiplying
arr1 = np.random.randint(-10, 10, (3, 2))  # Changing sizes of matrices
arr2 = np.random.randint(-10, 10, (2, 4))  # To show that mathematical multiplication works correctly
print(f'First matrix:\n{arr1}\nSecond matrix:\n{arr2}')
arr3 = np.matmul(arr1, arr2)
print(f'EXAMPLE OF THOSE MULTIPLIED MATRICES:\n{arr3}')  # We need it to compare the results
arr3 = np.zeros((len(arr1), len(arr2[0])), int)
if len(arr1[0]) == len(arr2):
    for i in range(len(arr1)):
        for u in range(len(arr2[0])):
            temp = 0
            for j in range(len(arr2)):
                temp += arr1[i, j] * arr2[j, u]
            arr3[i, u] = temp
else:
    print("Those matrices can't be multiplied mathematically.")
print(f'Multiplied matrices:\n{arr3}')

# Task 4
# Напишіть програму, що у матриці 4*4 змінює всі від’ємні елементи на 0
# Without numpy
arr = np.random.randint(-100, 100, (4, 4))
print(f'Matrix:\n{arr}')
for i in range(len(arr)):
    for u in range(len(arr[0])):
        if arr[i, u] < 0:
            arr[i, u] = 0
print(f'Edited matrix:\n{arr}')
# Using numpy .where()
arr = np.random.randint(-100, 100, (4, 4))
print(f'Matrix:\n{arr}')
arr = np.where(arr < 0, 0, arr)
print(f'Edited matrix:\n{arr}')
