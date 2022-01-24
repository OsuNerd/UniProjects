# Написати програму на мові Python, яка обчислює значення функції y = (5x2-3x) / sin(x) для значень x, що змінюються від 1 до 30, з кроком 0.5.
import math
for i in range(2, 61):
    print( (5 * (i / 2) * 2 - 3 * (i / 2)) / math.sin(i / 2) )
    print(i / 2)
# or
x = 1
while x < 30:
    print((5 * x * 2 - 3 * x) / math.sin(x))
    x += 0.5

# Написати програму на мові Python, що виводить в стандартний потік виведення кількість чисел, які кратні 4.
print("Чисел, які кратні 4 icнує безліч")
# Чисел кратних 4 - безліч, тому у користувача буде можливість обрати ліміти.
u = input("Введіть цілий нижній ліміт (включно): ")
l = input("Введіть цілий верхній ліміт (включно): ")
result = 0
if int(u) > int(l):
    print("Ви ввели некорректні ліміти")
else:
    for i in range(int(u), int(l)+1):
        if i % 4 == 0:
            result += 1
print(f"У вашому проміжку є {result} чисел, кратних 4.")

# Написати програму на мові Python, яка видаляє в заданому непорожньому тексті всі пари букв виду abab.
# Результуючий текст вивести на екран монітора.
text = "Мама кукушка кукушонку купила капюшон. Надел кукушонок капюшон. ыхых"
text1 = str(text)
# Вбираємо верхній регістр
text1 = text1.lower()
text1 = list(text1)
text = list(text)
result = ""
done = 0
while done == 0:
    counter = 0
    lenght = len(text1) - 3
    for i in range(len(text1)):
        if i + 3 >= len(text1):
            break
        else:
            first = str(text1[i])
            second = str(text1[i + 1])
            third = str(text1[i + 2])
            fourth = str(text1[i + 3])
            if first == third and second == fourth:
                for delete in range(4):
                    text1.pop(i)
                    text.pop(i)
            else:
                counter += 1
            continue
    if counter == lenght:
        done = 1
for i in text:
    result += i
print(result)

# Написати програму на мові Python, яка виводить в стандартний потік виведення всі прості числа від 1 до 1000.
# Примітка: просте число - це число, яке ділиться без остачі тільки на одиницю або саме на себе.
result = []
for i in range(1, 1001):
    counter = 1
    for u in range(1, i+1):
        if i % u == 0:
            counter += 1
    if counter == 3:
        result.append(str(i))
print(", ".join(result))
