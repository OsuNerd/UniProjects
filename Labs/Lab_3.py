# 3 Integer numbers input; Operator %
integer_numbers = []
print("Input some integer numbers")
for i in range(1, 4):
    integer_numbers.append(int(input(f'Integer number #{i}: ')))
# Output
for i, a in zip(integer_numbers, range(1, 4)):
    print('Result #{}:'.format(a), '%4.0f' % i)

# 3 Real numbers input; str.format() and f'
real_numbers = []
print("Input some real numbers")
for i in range(1, 4):
    real_numbers.append(float(input('Real number #{}: '.format(i))))
# Output
# str.format()
for i, a in zip(real_numbers, range(1, 4)):
    print('Floating point result #{}'.format(a), '{0:9}'.format(i))
# f'
for i, a in zip(real_numbers, range(1, 4)):
    print('Fixed point result #{}'.format(a), f'{i:6.3f}')

# 3 string symols in a line;
string_value = input("Input any symbols (string): ")
counter = int(0)
for i in string_value:
    counter += 1
for i in range(0, int(-(-counter//3))):
    print(string_value[i*3:(i*3+3)])

# Boolean
print(bool(0))
print(bool())
