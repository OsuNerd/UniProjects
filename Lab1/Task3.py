# Write a Python-script that detects the last 4 digits of a credit card.
credit_number = 7355608323548925
print(credit_number)
digits = []
for i in range(4):
    digits.append(credit_number//(10**(3-i)) % 10)
print(digits)
# [8, 9, 2, 5]

# converting into String format
digits2 = ''
for i in digits:
    digits2 += str(i)
print(digits2)
# 8925



# Find the sum of the digits of a three-digit number
num = 631
summ = int(0)
digit_amount = 3
while digit_amount > 0:
    summ += num // 10 ** (digit_amount - 1) % 10
    digit_amount -= 1
print(f'3-digit number: {num}')
print(f'Sum of 3 digits: {summ}')
# 3-digit number: 631
# Sum of 3 digits: 10
