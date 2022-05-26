import time
import numpy as np

comparisons = 0
swaps = 0

# Sorting functions
def bubble_sort(array, way=1):
    global comparisons, swaps
    amount = len(array) - 1
    while True:
        counter = 0
        for i, u in zip(array, range(amount)):
            comparisons += 1
            if way * i > way * array[u + 1]:
                swaps += 1
                array[u], array[u + 1] = array[u + 1], array[u]
                counter = 1
        comparisons += 1
        if counter == 0:
            return array

def selection_sort(array, way=1):
    global comparisons, swaps
    for i in range(len(array)):
        lowest_index = i
        for u in range(0+i, len(array)):
            comparisons += 1
            if way * array[lowest_index] >= way * array[u]:
                lowest_index = u
        swaps += 1
        array[i], array[lowest_index] = array[lowest_index], array[i]
    return array

def insertion_sort(array, way=1):
    global comparisons, swaps
    for i in range(1, len(array)):
        u = i - 1
        element = array[i]
        comparisons += 2
        while u >= 0 and way * element < way * array[u]:
            comparisons += 2
            swaps += 1
            array[u+1] = array[u]
            u = u-1
        array[u+1] = element
    return array

# Testing functions
def bubble_test(array, way=1):
    global comparisons, swaps
    comparisons, swaps = 0, 0
    ArrayToSort = array.copy()
    time0 = time.perf_counter()
    bubble_sort(ArrayToSort, way)
    time1 = time.perf_counter()
    timed = time1-time0
    return [comparisons, swaps, timed]

def selection_test(array, way=1):
    global comparisons, swaps
    comparisons, swaps = 0, 0
    ArrayToSort = array.copy()
    time0 = time.perf_counter()
    selection_sort(ArrayToSort, way)
    time1 = time.perf_counter()
    timed = time1-time0
    return [comparisons, swaps, timed]

def insertion_test(array, way=1):
    global comparisons, swaps
    comparisons, swaps = 0, 0
    ArrayToSort = array.copy()
    time0 = time.perf_counter()
    insertion_sort(ArrayToSort, way)
    time1 = time.perf_counter()
    timed = time1-time0
    return [comparisons, swaps, timed]


# Creating arrays
arr1 = np.random.randint(-100_000, 100_000, 100_000)  # Fully random array. Recommended lowering the third value to 3000
arr2 = arr1.copy()
arr2.sort()
arr3 = arr1.copy()
arr3 = -np.sort(-arr3)
custom_array = []
if input("Do you want to create your own array? Y/N ") == "Y":
    custom_array = [int(x) for x in ((input("Please, enter 30 or less integer values divided by space: ")).split())]
    print(f'Your array: {custom_array}')
    print(f'Your sorted ascending array: {bubble_sort(custom_array)}')
    print(f'Your sorted descending array: {bubble_sort(custom_array, -1)}')
    comparisons, swaps = 0, 0

results = [[], [], []]  # Creating list with sublists for each sorting algorithm

# Filling the results by testing
results[0].append(bubble_test(arr1))
results[0].append(bubble_test(arr2))
results[0].append(bubble_test(arr3))
results[1].append(selection_test(arr1))
results[1].append(selection_test(arr2))
results[1].append(selection_test(arr3))
results[2].append(insertion_test(arr1))
results[2].append(insertion_test(arr2))
results[2].append(insertion_test(arr3))
# ALL ALGORITHMS SORTING IN ASCENDING ORDER
# SORTING IN DESCENDING CAN BE DONE BY ADDING OPTIONAL PARAMETER "-1" LIKE THIS (arr, -1), FOR EXAMPLE:
# results[0].append(bubble_test(arr1, -1))

# Outputting the results
SortingMethod = ["Bubble sort", "Selection sort", "Insertion sort"]
Arrays = ["random array", "sorted ascending array", "sorted descending array"]
print()
for i in range(len(SortingMethod)):
    print(f'\n{SortingMethod[i]}.')
    for u in range(len(results[i])):
        print(f'In {Arrays[u]} it took {results[i][u][0]} comparisons, {results[i][u][1]} swaps and'
              f' {results[i][u][2]:0.10f} seconds')
print("\n\nRaw results list:", results)
