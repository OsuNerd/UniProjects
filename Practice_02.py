# Task 1

# Assume that we define x, y, and z to refer to int values. Write an expression that computes whether...

print("Please, input integer values for x, y and z.")
x, y, z = int(input("x is: ")), \
          int(input("y is: ")), \
          int(input("z is: "))
print(x, y, z)

# ...x is odd
# ...x is a multiple of 20 (e.g., 20, 40, 60, ...)

if x % 2 != 0:
    print("x is odd.")
else:
    print("x isn't odd.")

if x % 20 == 0:
    print("x is a multiple of 20")
else:
    print("x is NOT a multiple of 20.")

# Assume that zero is a positive number. Write an expression that computes whether...
# ...x and y are both positive
# ...x and y have the same sign (both are positive or both are negative)
# ...x and y have different signs (one is positive and one is negative)

if x >= 0 and y >= 0:
    print("x and y are both positive.")
else:
    print("x and y aren't both positive.")

if (x >= 0) == (y >= 0) and (x >= 0) is True:
    print("x and y have the same positive sign.")
elif (x >= 0) == (y >= 0) and (x >= 0) is False:
    print("x and y have the same negative sign.")
else:
    if x >= 0:
        print("x and y have different signs. x is positive, while y is negative.")
    else:
        print("x and y have different signs. x is negative, while y is positive.")

# Write an expression that computes whether...
# ...all three names (x, y, and z) are bound to equal values
# ...all three names (x, y, and z) are bound to different values (none the same)
# ...two variables store the same value, but the third one is different

if x == y == z:
    print("All three variables are bound to equal value.")
elif x != y and z != y and x != z:
    print("All three variable are bound to different values.")
elif x == y or y == z or x == z and x != y or y != z or x != z:
    print("Two variables store the same value, but the third one is different.")

print("________________________________________________________________________")

# Task 2
# Assume that we specify two points in space by defining the x and y coordinate of each using x1, y1, x2, and y2 all
# which are float. Write an expression that computes...

x1, y1 = float(input("Input x1: ")), \
         float(input("Input y1: "))
x2, y2 = float(input("Input x2: ")), \
         float(input("Input y2: "))

# ...the distance between these points
# Distance between two points formula: d = √[(x2-x1)^2+(y2-y1)^2]

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between two points:", + distance)
# print(f'{distance:.3f}')

# ...the slope of the line from the first point to the second
# Slope formula between two points: m = (y2-y1)/(x2-x1)

if x2 - x1 == 0:
    print("Division by zero is undefined.")
else:
    slope = (y2 - y1) / (x2 - x1)
    print(f"Slope between two points is: {slope}")

# ...whether both points lie on the same line from the origin

# Version 1

if x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0:
    slope1 = slope2 = 1
elif (x1 - 0) != 0 and (x2 - 0) != 0:
    slope1 = (y1 - 0) / (x1 - 0)
    slope2 = (y2 - 0) / (x2 - 0)
elif (x1 - 0) == 0 and (x2 - 0) == 0:
    slope1 = (y1 - 0) / 1
    slope2 = (y2 - 0) / 1
elif (x1 - 0) == 0 and (x2 - 0) != 0:
    slope1 = (y1 - 0) / 1
    slope2 = (y2 - 0) / (x2 - 0)
elif (x1 - 0) != 0 and (x2 - 0) == 0:
    slope1 = (y1 - 0) / (x1 - 0)
    slope2 = (y2 - 0) / 1

if slope1 == slope2:
    print("Both points lie on the same line from the origin.")
else:
    print("Both points don't lie on the same line from the origin.")

# Version 2

vector_ox1 = x1 - 0
vector_ox2 = x2 - 0
vector_oy1 = y1 - 0
vector_oy2 = y2 - 0
cross = vector_ox1 * vector_oy2 - vector_ox2 * vector_oy1
if cross == 0:
    print("V.2.: Both points lie on the same line from the origin.")
else:
    print("V.2.: Both points don't lie on the same line from the origin.")

# ...whether the first point is above the second

if y1 > y2:
    print("First point is above the second.")
elif y1 == y2:
    print("First point has the same height (y) as the second.")
else:
    print("First point is below the second.")

# ...what quadrant the first point lies in (1st, 2nd, 3rd, or 4th)

if x1 == 0 and y1 == 0:
    print("First point is right on the origin.")
elif x1 >= 0:
    if x1 == 0:
        if y1 > 0:
            print("First point lies between 1rst and 2nd quadrant on y axis.")
        else:
            print("First point lies between 3rd and 4th quadrant on y axis.")
    elif x1 > 0:
        if y1 > 0:
            print("First point lies in 1rst quadrant.")
        elif y1 < 0:
            print("First point lies in 4th quadrant.")
        else:
            print("First point lies between 1rst and 4th quadrant on x axis.")
elif x1 < 0:
    if y1 > 0:
        print("First point lies in 2nd quadrant.")
    elif y1 < 0:
        print("First point lies in 3rd quadrant.")
    else:
        print("First point lies between 2nd and 3rd quadrant on x axis.")


# ...whether the two points lie in the same quadrant

# done with using matrix, which will represent location of the point
pos = ""


def position(x_, y_):
    quadrant_matrix = []
    for i in range(3):
        quadrant_matrix.append([0] * 3)
    if x_ == 0:
        for i in range(3):
            quadrant_matrix[i][1] += 1
    elif x_ > 0:
        for i in range(3):
            quadrant_matrix[i][2] += 1
    elif x_ < 0:
        for i in range(3):
            quadrant_matrix[i][0] += 1
    if y_ == 0:
        for i in range(3):
            quadrant_matrix[1][i] += 1
    elif y_ > 0:
        for i in range(3):
            quadrant_matrix[0][i] += 1
    elif y_ < 0:
        for i in range(3):
            quadrant_matrix[2][i] += 1
    row = -1
    for r in quadrant_matrix:
        row += 1
        column = -1
        for c in r:
            column += 1
            if c > 1:
                pos = [row, column]
    return pos


dictionary = {"[0, 0]": "2nd quadrant", "[0, 1]": "Between 2nd and 1rst", "[0, 2]": "1rst quadrant",
              "[1, 0]": "Between 2nd and 3rd", "[1, 1]": "On origin", "[1, 2]": "Between 1rst and 4th quadrant",
              "[2, 0]": "3rd quadrant", "[2, 1]": "Between 3rd and 4th", "[2, 2]": "4th quadrant"}

pos1 = position(x1, y1)
print(f'Position of the first point: {dictionary.get(str(pos1))}')
pos2 = position(x2, y2)
print(f'Position of the second point: {dictionary.get(str(pos2))}')

if pos1 == pos2:
    print("Points are in the same quadrant or place.")
else:
    print("Points are in different quadrants or places.")
