import string
# а) Розглянемо послідовність, утворену дробами: 1/1, 2/1, 3/2, ..., в якій чисельник (знаменник) наступного члена
# послідовності виходить складанням чисельників (знаменників) двох попередніх членів.
#
# Чисельники двох перших дробів рівні 1 і 2, знаменники - 1 і 1.
# ·          Знайти k-й член цієї послідовності.
# ·          Отримати перші n членів цієї послідовності..

x = [1, 2]
y = [1, 1]
k = int(input("k: "))
n = int(input("n: "))
if k >= 3:
    for i in range(k-2):
        x.append(int(x[-1]) + int(x[-2]))
        y.append(int(y[-1]) + int(y[-2]))
    print(f'{x[-1]}/{y[-1]}')
elif k == 2:
    print("K is 2/1")
elif k == 1:
    print("K is 1/1")
for i in range(n):
    if i == n-1:
        print(f'{x[i]}/{y[i]}')
    else:
        print(f'{x[i]}/{y[i]}', end=", ")

# б) Програма. Дана послідовність, що містить від 2 до 20 слів, в кожному з яких від 1 до 8 малих літер, між сусідніми
# словами - не менше одного пробілу, за останнім словом - крапка. Вивести на екран ті слова послідовності, які відмінні
# від останнього слова і в слові немає повторюваних букв Звернення за індексом до елементів рядків в завданнях
# підпункту б) не застосовується.

text = ("god dog bible  pencill  scissors bomb pencill.".split("."))
text = (" ".join(text)).split()
length = len(text)
text1 = []
last_word = []
for i, u in zip(range(length), text):
    if i + 1 != length:
        text1.append(u)
    else:
        last_word.append(u)
result = []
for i in text1:
    if str(i) not in str(last_word):
        for a in i:
            result += a
        print(i, end=" ")
print()
print(set(result))


# в) Дано два слова. Визначити, чи можна з букв першого з них здобути друге. Розглянути варіант, коли букви другого
# слова, що повторюються, можуть в першому слові не повторюватися.

first_word = "Pepssssiiiimax"
second_word = "Mississippi"
for u, y in zip(string.ascii_uppercase, string.ascii_lowercase):
    first_word = first_word.replace(u, y)
    second_word = second_word.replace(u, y)
# repeating characters
print("Yes, it's possible." if set(second_word)-set(first_word) == set() else None)
# non-repeating characters
first = []
for i in first_word:
    first.append(i)
second = []
for i in second_word:
    second.append(i)
counter = 0
clear = 0
while clear == 0:
    for i in first:
        for a in second:
            if i == a:
                first.pop(first.index(i))
                second.pop(second.index(a))
                break

    for i in first:
        for a in second:
            if i == a:
                continue
            else:
                counter += 1
        continue
    if counter >= len(first)*len(second):
        clear = 1
    counter = 0
    if second == []:
        clear = 1


if second != []:
    print("No, it's impossible with non-repeating characters.")
else:
    print("Yes, it's possible with non-repeating characters.")
