num=int(input('Enter your number: '))
summ,diff,prod=int(0),\
                int(0),\
                int(1)
def n(number):
    counter = 0
    cnumber = number
    while cnumber > 0:
        cnumber //= 10
        counter += 1
    return counter
digit=int(n(num))
digit_calc=digit
while digit_calc>0:
    summ += num//10**(digit_calc-1) %10
    prod *= num//10**(digit_calc-1) %10
    diff -= num//10**(digit_calc-1) %10
    digit_calc -= 1
print(f"Digits:  {digit}")
print(f'Sum of digits: {summ}')
print(f'Difference of digits: {diff}')
print(f'Product of digits: {prod}')  
input("Press ENTER to exit")
