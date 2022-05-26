import numpy as np
import random

def linear_search(arr, element):
    global counter
    for i in range(len(arr)):
        counter += 1
        if element == arr[i]:
            return i
    return -1

def binary_search(arr, element):
    global counter
    beg, end = 0, len(arr)-1
    while beg <= end:
        middle = (beg+end) // 2
        counter += 1
        if element < arr[middle]:
            end = middle - 1
        else:
            counter += 1
            if element > arr[middle]:
                beg = middle + 1
            else:
                return middle
    return -1

def substring_search(text: str, element: str):
    global counter
    i = -1
    j = 0
    while (j < len(element)) and i < (len(text) - len(element)):
        j = 0
        i += 1
        counter += 2
        while j < len(element) and element[j] == text[i + j]:
            j += 1
            counter += 2
    counter += 1
    if j == len(element):
        return i
    return -1


# Part 1

counter = 0
arr = np.random.randint(-1000, 1000, 1000)
indexes = [random.randint(0, 999), random.randint(0, 999), random.randint(0, 999)] # Randomly choosing indexes
el1 = [arr[indexes[0]], arr[indexes[1]], arr[indexes[2]]] # Taking elements that we can later search
el1_indexes = []
print("Indexes of searched elements:", indexes[0], indexes[1], indexes[2])
print("Respective elements:", el1[0], el1[1], el1[2])

linear_counter = []
binary_counter = []
substring_counter = []
print("\nLinear search")
for i in el1:
    found_index = linear_search(arr, i)
    if found_index >= 0:
        el1_indexes.append(found_index)
        found_element = arr[found_index]
        print(f'Found element ({found_element}) at index {found_index}.')
        linear_counter.append(counter)
        counter = 0
    else:
        print(f'Element {i} wasn\'t found in array.')

# Part 2

arr.sort()  # sorting the array for binary search
el2 = [arr[indexes[0]], arr[indexes[1]], arr[indexes[2]]] # Taking elements to search
el2_indexes = []
print("\nIndexes of searched elements:", indexes[0], indexes[1], indexes[2])
print("Elements with the same index after sorting:", el2[0], el2[1], el2[2])
print("\nBinary search")

for i in el2:
    found_index = binary_search(arr, i)
    if found_index >= 0:
        el2_indexes.append(found_index)
        found_element = arr[found_index]
        print(f'Found element ({found_element}) at index {found_index}.')
        binary_counter.append(counter)
        counter = 0
    else:
        print(f'Element {i} wasn\'t found in array.')

# Part 3

print("\nSubstring search")
text = "Карл у Клары украл кораллы, а Клара у Карла украла кларнет."
el3 = ["Карл", "а К", "рала"]
el3_indexes = []
for i in el3:
    found_index = substring_search(text, i)
    if found_index >= 0:
        el3_indexes.append(found_index)
        found_element = text[found_index]
        print(f'Found element ({i}) at index {found_index}.')
        substring_counter.append(counter)
        counter = 0
    else:
        print(f'Element {i} wasn\'t found in array.')


########################################################################################################################
#                                               Summary

print("\n", "*"*40, "\n\nTotal results")

print("For Linear search:")
for i, u in zip(linear_counter, range(len(el1))):
    print(f'It took {i} comparisons to find element ({el1[u]}) at index {el1_indexes[u]}.')

print("\nFor Binary search:")
for i, u in zip(binary_counter, range(len(el2))):
    print(f'It took {i} comparisons to find element ({el2[u]}) at index {el2_indexes[u]}.')

print("\nFor Substring search:")
for i, u in zip(substring_counter, range(len(el3))):
    print(f'It took ~{i} comparisons to find element ({el3[u]}) at index {el3_indexes[u]}.')


