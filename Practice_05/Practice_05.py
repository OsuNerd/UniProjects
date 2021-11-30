import string
# Write a Python program to generate and print a list, where the values are square of numbers between 1 and 30
# (both included)

list1 = []
for i in range(1, 31):
    list1.append(i**2)
print(list1)

# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# For some reason i though i must extract the date from a file so here we are

with open("exam_st_date.txt", "r") as r:
    for i in r.readlines():
        if "exam_st_date" in i:
            exam_st_date = i

for i in (string.punctuation + string.ascii_letters):
    while i in exam_st_date:
        exam_st_date = exam_st_date.replace(i, " ")

exam_st_date = "/".join(exam_st_date.split())
print(f"Your exam date is: {exam_st_date}")

# Another version
exam_st_date = (11, 12, 2014)
exam_st_date = " / ".join([str(i) for i in exam_st_date])
print(f"Your exam date is: {exam_st_date}")

# Write a Python program which accepts a sequence of comma separated numbers from user and generate a list and a tuple
# with those numbers.
# Sample data : 3, 5, 7, 23
# Output:
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

inp = input("Enter comma separated numbers: ").replace(",", " ")
list0 = inp.split()
tupl = tuple(inp.split())
print(list0, "\n", tupl)

# Write a Python function that takes two lists and returns True if they have at least one common member.

list1 = [1, 2, 3, 4, 5, "br"]
list2 = [6, 7, 8, 10, 22, "b r", "br ", 1.0]

for i in list1:
    if i in list2:
        print(bool(1))
        break

# Write a Python-script.
#
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
#
# You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which
# represent number of people get into bus (The first item) and number of people get off the bus (The second item)
# in a bus stop.
#
# Your task is to return number of people who are still in the bus after the last bus station (after the last array).
# Even though it is the last bus stop, the bus is not empty and some people are still in the bus,
# and they are probably sleeping there :D
#
# Example:
#
# number([[10,0],[3,5],[5,8]]) # Result is 5
# number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) # Result is 17
# number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) # Result is 21

number = [[7, 0], [8, 1], [2, 5], [4, 6], [6, 3], [2, 1]]
people = 0
for i in number:
    people = people + i[0] - i[1]
    if people < 0:
        people = 0
print(f'People left: {people}')
