# Варіант 10
# ·        Ціле число – хвилини
# ·        Ціле число – години
# Обчислити кількість хвилин до опівночі
# Збільшити заданий час на 107 хвилин та вивести новий час на екран

# If values are gonna exceed 60 minutes, i will try to convert minutes into hours and minutes and add them.
# In case of hours exceeding 24, i will start the hours over from 0, as if it hit the midnight and kept going.
class Time:
    def __init__(self, hours: int = 12, mins: int = 0):
        if mins < 0 or hours < 0:
            raise ValueError("Entered values can not be negative.")

        self.mins = mins
        self.hours = hours

        self.convert()

    def convert(self):
        if self.mins >= 60:
            self.hours = self.hours + (self.mins // 60)
            self.mins = self.mins % 60
        if self.hours >= 24:
            self.hours = self.hours % 24

    def till_midnight(self):
        return (24 - self.hours) * 60 - self.mins if (self.hours != 0 or self.mins != 0) else 0

    def add107(self):
        mins = self.mins + 107
        hours = self.hours

        if mins >= 60:
            hours = hours + (mins // 60)
            mins = mins % 60
        if hours >= 24:
            hours = hours % 24

        return f"{hours:02d}:{mins:02d}"

    def __str__(self):
        return f"Your time is {self.hours:02d}:{self.mins:02d}. " \
               f"You have {self.till_midnight()} minutes until midnight.\n" \
               f"107 minutes later after your time is {self.add107()}"


x1 = [Time(), Time(16, 30), Time(17, 30), Time(17, 10), Time(17, 0), Time(23, 59), Time(0, 0), Time(0, 1), Time(0, 59)]

for i in x1:
    print(i)

print("\n", "*"*80, "\n")

# console application part
while True:
    x = int(input("Please, enter an integer for hours (entering wrong value will result in an error): "))
    y = int(input("Please, enter an integer for minutes (entering wrong value will result in an error): "))

    x2 = Time(x, y)
    print(x2)

    if input("Enter 'e' to exit. Enter anything else to continue. ") == "e":
        break
