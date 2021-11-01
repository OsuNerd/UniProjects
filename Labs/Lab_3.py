# 3 Integer numbers input; All
integer_numbers = []
print("Input some integer numbers")
for i in range(1, 4):
    integer_numbers.append(int(input(f'Integer number #{i}: ')))

# Output
# % Operator
for i, a in zip(integer_numbers, range(1, 4)):
    print('% Result #{}:'.format(a), '%4d' % i)
# str.format()
for i, a in zip(integer_numbers, range(1,4)):
    print('str.format Result #{}:'.format(a), '{0:4}'.format(i))
# f'
for i, a in zip(integer_numbers, range(1, 4)):
    print("f' Result #{}:".format(a), f'{i:4}')


# 3 Real numbers input; All
real_numbers = []
print("Input some real numbers")
for i in range(1, 4):
    real_numbers.append(float(input('Real number #{}: '.format(i))))

# Floating Output
# % Operator
for i, a in zip(real_numbers, range(1, 4)):
    print('% Floating point result #{}:'.format(a), '%9s' % i)
# str.format()
for i, a in zip(real_numbers, range(1, 4)):
    print('Floating point result #{}:'.format(a), '{0:9}'.format(i))
# f'
for i, a in zip(real_numbers, range(1, 4)):
    print("f' Floating point result #{}:".format(a), f'{i:9}')

# Fixed poing Output
# % Operator
for i, a in zip(real_numbers, range(1, 4)):
    print('Fixed point result #{}:'.format(a), '%6.3f' % i)
# str.format()
for i, a in zip(real_numbers, range(1, 4)):
    print('Fixed point result #{}:'.format(a), '{0:6.3f}'.format(i))
# f'
for i, a in zip(real_numbers, range(1, 4)):
    print('Fixed point result #{}:'.format(a), f'{i:6.3f}')


# 3 string symols in a line;
string_value = input("Input any symbols (string): ")
counter = int(0)
for i in string_value:
    counter += 1
for i in range(0, int(-(-counter//3))):
    print(string_value[i*3:(i*3+3)])

# Boolean
print(bool(0))
# or
print(bool())
