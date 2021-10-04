# Integer zero
q = 0
print(q, type(q))

# Floating point zero
w = float(0)
print(w, type(w))

# Integer one hundred and one
e = 101
print(e, type(e))

# Floating point one thousand
r = float(1000)
print(r, type(r))

# Floating point one thousand using scientific notation
t = 1E3
print(t, type(t))

# Create a positive integer, a negative integer, and zero. Assign them to variables
y = 15
u = -15
i = 0
print(y, type(y), '___', u, type(u), '___', i, type(i))

# Write several arithmetic expressions. Bind the values to variables. Use a variety of operators, e.g. +, -, /, *, etc.
# Use parentheses to control operator scope.
p = 8 * 3 + 5 - (3 - 1)
a = 40 - 5 * (5 + 3)
print(p, type(p), '___', a, type(a))

# Create several floats and assign them to variables.
s = float(5)
d, f = float(7), \
       99.9
print(s, type(s), '___', d, type(d), '___', f, type(f))

# Write several arithmetic expressions containing your float variables.
print(f + d - s)
print(f * s + d * s)

# Write several expressions using mixed arithmetic (integers and floats).
g = 3.5 + 4 - 7 * 1.5 / 8
h = 8 * 5.5 - 5 * 6
print(g, type(g), '___', h, type(h))

# Obtain a float as a result of division of one integer by another; do so by explicitly converting one integer
# to a float.
j = 3 / float(2)
print(j, type(j))
