# 1. Написати програму, яка змінює значення двох цілих змінних a і b без
# використання додаткових змінних.
a = 6
b = 35
a = a + 12
b = 100 - b
print(a, b)

# 2. Написати програму, яка обчислює і виводить на екран:
# • середнє арифметичне двох цілих чисел a і b;
# • середнє геометричне двох цілих чисел a і b.
a = int(input("Integral a = "))
b = int(input("Integral b = "))
print(f'Average of a and b: {(a+b)/2}')
print(f'Geometric average of a and b: {(a*b)**0.5}')

# 3. Написати програму, яка переставляє цифри трьохзначного числа, яке задане
# користувачем у зворотному порядку і виводить нове число на екран.
number = int(input("Input a natural three-digit number: "))
digits = ""
for i in range(1, 4):
    digits = str((number//(10**(3-i)) % 10)) + digits
print(f'Reverse: {digits}')

# 4. Написати програму, яка визначає загальну кількість годин доби (змінна hour) і
# загальну кількість хвилин доби (змінна minute), які пройшли до моменту поточної
# секунди доби (змінна second). Наприклад, якщо second = 11111 (second = 3 * 3600
# + 5 * 60 + 11), то hour = 3 і minute = 5.
seconds = float(input("Seconds: "))
minutes = seconds//60
hours = minutes//60
print(f'{hours} hours equals to {minutes} minutes equals to {seconds} seconds.')
print(f'Hours: {hours}, Minutes: {minutes % 60}, Seconds: {(seconds % 60) % 60}.')

# 5. Написати програму, яка визначає значення кута в градусах (змінна corner) між
# станом годинникової стрілки на початку доби і її станом в hour годин, minute
# хвилин і second секунд (0 ≤ hour ≤ 11; 0 ≤ minute; second ≤ 59).
print("Input hour, minute and second of hour hand (часовой стрелки/годинникової стрілки.)")
hours = int(input("Input hours: ")) % 12
minutes = int(input("Input minutes: "))
seconds = int(input("Input seconds: "))
corner = float(0)
for i in range(hours):
    corner += 30
for i in range(minutes):
    corner += 0.5
for i in range(seconds):
    corner += (0.5 / 60)
print(f'There are {corner}° degrees between hour hand at the start of the day and hour hand with your values '
      f'(clockwise).')

# Написати програму яка визначає чи є натуральне число, що ввів користувач:
# • парним;
# • таким, що закінчується на цифру 5.
natural = int(input("Please input a natural number: "))
while natural < 0:
    natural = int(input("Your number isn't natural \nPlease enter a valid number: "))
if natural // 2 == 0:
    print(f"Your natural number {natural} is even.")
else:
    print(f"Your natural number {natural} is odd.")
while natural > 10:
    natural = natural % 10
if natural == 5:
    print("Your number ends with 5")
else:
    print("Your number doesn't end with 5")

# Написати програму, яка визначає значення цілої змінної number - від 1 до 7, в
# залежності від того, на який день тижня (від понеділка до неділі) припадає день
# (ціла змінна day) невисокосного року, в якому 1 січня - понеділок (1 ≤ day ≤ 365).
day = int(input("Input your day of the year from 1 to 365: "))
while 1 > day or day > 365:
    day = int(input("Your input is invalid, please enter a valid day from 1 to 365: "))
dictionary = {1: "Monday - Понеділок - Понедельник", 2: "Tuesday - Вівторок - Вторник",
              3: "Wednesday - Середа - Среда", 4: "Thursday - Четвер - Четверг",
              5: "Friday - П'ятниця - Пятница", 6: "Saturday - Субота - Суббота",
              7: "Sunday - Неділя - Воскресенье"}
number = day % 7 if day % 7 != 0 else 7
# print(f"Your day of the week is: {dictionary.get(day % 7 if day % 7 != 0 else 7)}")
print(f"Your day of the week is: {dictionary.get(number)}")

# Написати програму, яка визначає можливість побудови трикутника для заданих
# довільними дійсними числами довжин сторін. Програма виводить True або False
a, b, c = float(input("Enter value for the first side a: ")), \
          float(input("Enter value for the second side b: ")), \
          float(input("Enter value for the third side c: "))
if a < b + c and b < a + c and c < a + b:
    print(bool(1))
else:
    print(bool(0))
