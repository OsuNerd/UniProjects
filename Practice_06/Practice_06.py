# Task #1: Write a Python program to calculate the length of a string.

text = input("Please, enter some text: ")
print(f'The length of your text is: {len(text)}')
# or
counter = 0
for i in text:
    counter += 1
print(f'The length of your text is: {counter}')

# Task #2: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead the empty string.
# Sample Strings:
# 'w3resource' Expected Result : 'w3ce'
# 'w3' Expected Result : 'w3w3'
# 'w' Expected Result : Empty String

text1 = input("Please, enter some text: ")
if len(text1) >= 2:
    print(text1[0:2] + text1[-2:])
else:
    print()

# Task #3: Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself. Sample String : 'restart' Expected Result : 'resta$t'

text2 = input("Please, enter some text: ")

print(f'Result: {text2[0]}{text2[1:].replace(text2[0], "$")}')

# Task #4: Write a Python function to reverses a string if it's length is a multiple of 4.

text3 = input("Please, enter some text: ")
print(text3[::-1] if len(text3)%4 == 0 else text3)
# or
if len(text3)%4 == 0:
    text3 = text3[::-1]
print(text3)

# Task #5: Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
# in sorted form (alphanumerically). Sample Words : red, white, black, red, green, black Expected Result:
# black, green, red, white, red

text4 = input("Please, enter some comma separated sequence of words: ")
words = sorted(set(text4.replace(",", " ").split()))
print(f'Result: {", ".join(words)}')
