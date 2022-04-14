import numpy as np

# Створити матрицю 10 на 20 з числами від 0 до 15 / Create a 10 by 20 matrix with random numbers from 0 to 15

i = np.random.randint(0,15, (10,20))

# Закоментований спосіб створення матриці без використання бібліотеки Numpy
# Commented way of creating a matrix without Numpy library
# i = []
# for u in range(10):
#     i.append(list())
# for u in i:
#     for y in range(20):
#         u.append(random.randint(0,15))

# Вивести матрицю на екран: / Display the matrix on screen:

for u in i:
    print(u)

# Вивести номери рядків, які містять 3 та більше чисел 5 / Output sequentional number of rows that have 3 or more numbers 5

rowsNumber = []
counter = 0
for (r, u) in zip(range(1,11), i):
    for y in u:
        if y == 5:
            counter += 1
    if counter >= 3:
        rowsNumber.append(str(r))
    counter = 0
print(f'Номери рядків з трьома та більше чисел 5: {", ".join(rowsNumber) if rowsNumber != [] else "Таких рядків немає."}')
