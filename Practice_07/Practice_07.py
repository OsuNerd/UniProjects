import string
# Task 1: Implement a script which receives a string and replaces all " symbols with ' and vise versa.
# The script should return modified string.
text = input("Please, enter some text with ' and \" symbols: ")
list0 = list(text)
for i, u in zip(list0, range(len(text))):
    if i == "'":
        list0[u] = '"'
    elif i == '"':
        list0[u] = "'"
print("".join(list0))

# Task 2
# Write a script that checks whether a string is a palindrome or not.
# Returns 'True' if it is palindrome, else 'False'.
# To check your implementation you can use strings from here
# (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
# The script has to ignore special characters, whitespaces and different cases

text1 = input("Please, enter some text: ")
text_palindrome = text1
# Ignoring (removing) whitespace
for i in (string.whitespace + string.punctuation):
    text_palindrome = text_palindrome.replace(i, "")
# Ignoring different cases (changing upper to lower)
for u, y in zip(string.ascii_uppercase, string.ascii_lowercase):
    text_palindrome = text_palindrome.replace(u, y)
print(text_palindrome)   # For convenience

if text_palindrome == text_palindrome[::-1]:
    print(bool(1))
else:
    print(bool(0))

# Task 3: # Implement a script which works the same as str.split
# Note: Usage of str.split method is prohibited

text2 = input("Please, enter some text: ")
split_char = input("Please, enter a splitting character (leave blank for splitting without specific character): ")

# Getting a sample to match
if split_char == "":
    sample = text2.split()
else:
    sample = text2.split(split_char)

counter = 1
result = []
i, u = 0, 0
if split_char != "":
    # Counting how many elements there should be in result
    for i in text2:
        if i == split_char:
            counter += 1

    # Adding those elements
    if text2 == "":
        result = []
    else:
        for i in range(counter):
            result.append("")

    # Resetting "i" value and adding symbols to the result values
    i = 0
    for u in text2:
        if u != split_char:
            result[i] += u
        else:
            i += 1

else:
    # Getting rid of useless spaces in a row, which str.split ignores when no splitting character given
    while "  " in text2:
        text2 = text2.replace("  ", " ")
    # Getting rid of spaces from  side
    for i in text2:
        if i == " ":
            text2 = text2[1:]
        else:
            break
    # And from right side
    for i in text2[::-1]:
        if i == " ":
            text2 = text2[:len(text2) - 1]
        else:
            break
    print(text2)   # Just for convenience
    # Counting how many elements there should be in result
    for i in text2:
        if i == " ":
            counter += 1

    # Adding those elements
    if text2 == "":
        result = []
    else:
        for i in range(counter):
            result.append("")

    # Resetting "i" value and adding symbols to the result values
    i = 0
    for u in text2:
        if u != " ":
            result[i] += u
        else:
            i += 1


print(counter)   # Just for convenience
print(f'{sample}\n{result}')   # Comparing actual str.split function with the result
i, u = 0, 0   # Resetting values just to be safe for the rest of code

# Task 4: Implement a script which returns the longest word in the given string.
# The word can contain any symbols except whitespaces (`,\n,\tand so on).
# If there are multiple longest words in the string with a same length return the word that occurs first.

text3 = input("Please, enter a sentence: ")
for i in string.whitespace:
    text3 = text3.replace(i, " ")
text3 = text3.split()
for i in text3:
    count = 0
    for u in text3:
        if len(i) >= len(u):
            count += 1
            pass
        else:
            continue
        if count >= len(text3):
            print(f'The longest word is: {i}')

# Task 5
# For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n. Example,
# n = 1234 result = 4
# n = 246 result = 0
n = int(input("Please, enter a positive integer number: "))
while n < 0 or n % 1 != 0:
    n = int(input("Please, enter a correct positive integer number: "))
summ = 0
for i in str(n):
    if int(i) % 2 != 0:
        summ += int(i)
print(f'The sum of odd numbers is {summ}')

# Task 6
# Create a script that for a positive integer n calculates the result value, which is equal to the sum of the “1”
# in the binary representation of n otherwise, returns None.
# Example,
# n = 14 = 1110 result = 3
# n = 128 = 10000000 result = 1

n = int(input("Please, enter a positive integer number: "))
if n < 0 or n % 1 != 0:
    print(None)
else:
    m = bin(n)[2:]
    result = 0
    for i in m:
        result += int(i)
    print(result)

# Task 7
# Write a script which will take an array of strings and returns an array of strings with the needless directions
# removed (W<->E or S<->N side by side).

path = []
proceed = "0"
# Making sure the input is right
while proceed != "1":
    text4 = input("Please, enter a path using 'N', 'E', 'S', 'W' for directions (one at a time), to proceed type '1':")
    if text4 == "1":
        proceed = "1"
    elif text4 == "N" or text4 == "E" or text4 == "S" or text4 == "W":
        path.append(text4)
    else:
        print("Please, write a correct direction ('N', 'E', 'S', 'W') or enter '1' to proceed.")

path_2 = list(path)
# way of destroying every direction the other way (not side by side)
while path.count("N") > 0 and path.count("S") > 0 or path.count("E") > 0 and path.count("W") > 0:
    for i in path:
        if i == "N":
            i = path.index("N")
            for u in path:
                if u == "S":
                    path.pop(i)
                    u = path.index("S")
                    path.pop(u)
        elif i == "E":
            i = path.index("E")
            for u in path:
                if u == "W":
                    path.pop(i)
                    u = path.index("W")
                    path.pop(u)

print(f'Your final path is: {path}')

# side by side
fdir = [['N', 'S'], ['S', 'N'], ['E', 'W'], ['W', 'E']]
clear = 0
counter = 0
count = 0
while clear == 0:
    count = 0
    for a in fdir:
        if str(a)[1:-1] in str(path_2):
            for i in path_2:

                index1 = path_2[counter:].index(a[0]) + counter
                if index1 < len(path_2) - 1:
                    index2 = index1 + 1
                else:
                    break
                if path_2[index1] == "N":
                    if path_2[index2] == "S":
                        path_2.pop(index1)
                        path_2.pop(index1)
                        counter = index1-1
                        break
                elif path_2[index1] == "S":
                    if path_2[index2] == "N":
                        path_2.pop(index1)
                        path_2.pop(index1)
                        counter = index1 - 1
                        break
                elif path_2[index1] == "E":
                    if path_2[index2] == "W":
                        path_2.pop(index1)
                        path_2.pop(index1)
                        counter = index1 - 1
                        break
                elif path_2[index1] == "W":
                    if path_2[index2] == "E":
                        path_2.pop(index1)
                        path_2.pop(index1)
                        counter = index1 - 1
                        break
    for a in fdir:
        if str(a)[1:-1] in str(path_2):
            break
        elif str(a)[1:-1] not in str(path_2):
            count += 1
    if count >= 4:
        clear = 1


print(f'Your final path is: {path_2}')

# Task 8
# You will be given a list of strings, a transcript of an English Shiritori match. Your task is to find out if the game
# ended early, and return a list that contains every valid string until the mistake. If a list is empty return an empty
# list. If one of the elements is an empty string, that is invalid and should be handled.

text5 = input("Write words for the game with space between them: ")
for u, y in zip(string.ascii_uppercase, string.ascii_lowercase):
    text5 = text5.replace(u, y)
text5 = text5.split(" ")
result = []
index = 0
for i in text5[:-1]:
    if i[-1:-2:-1] == text5[index+1][0:1]:
        result.append(i)
        index += 1
    elif i[-1:-2:-1] == "":
        break
    else:
        break
result.append(i)

print(result)
