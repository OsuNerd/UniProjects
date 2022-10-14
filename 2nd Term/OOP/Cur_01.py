# Задача 1. Розробити клас з даними про ПОГОДУ: дата, середня температура, атмосферний тиск, опади.
# Визначити конструктори, методи / властивості встановлення та читання значень полів даних.
# Визначити дні з найбільшим перепадом тиску.
from datetime import datetime

class Weather:
    instances = []

    def __init__(self, date, avg_temp: float, atm: float, precipitation: str):
        self.__date = date
        self.__avg_temp = avg_temp
        self.__atm = atm
        self.__precipitation = precipitation

        self.save()

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self.__date = (datetime.strptime(date, "%d/%m/%y"))
        elif not isinstance(date, datetime):
            raise ValueError("Wrong datatype for date.")
        else:
            self.__date = date

    @property
    def avg_temp(self):
        return self.__avg_temp

    @avg_temp.setter
    def avg_temp(self, avg_temp):
        if avg_temp < -273.15:
            raise ValueError("Temperature can't be lower than absolute zero (-273,15C).")
        else:
            self.__avg_temp = avg_temp

    @property
    def atm(self):
        return self.__atm

    @atm.setter
    def atm(self, atm):
        if atm < 0:
            raise ValueError("Atmospheric pressure cannot be negative.")
        else:
            self.__atm = atm

    @property
    def precipitation(self):
        return self.__precipitation

    def save(self):
        count = 0
        for i in self.__class__.instances:
            if i.date == self.__date:
                count += 1
        if count != 0:
            print("This date already exists in database.")
        else:
            self.__class__.instances.append(self)

            self.sort()

    def sort(self):
        count = 1
        if len(self.__class__.instances) >= 2:
            while count != 0:
                count = 0
                # can be optimized be reversing the sorting algorithm
                for i in range(len(self.__class__.instances)-1):
                    if self.__class__.instances[i].date > self.__class__.instances[i+1].date:
                        self.__class__.instances[i], self.__class__.instances[i+1] = self.__class__.instances[i+1], self.__class__.instances[i]
                        count += 1
            print("Sorting complete.")
        else:
            print("Not enough instances created to sort.")

    def __str__(self):
        return f'Date: {self.__date}\nAverage temperature: {self.__avg_temp}C; ATM: {self.__atm}; ' \
               f'Precipitation: {self.__precipitation}'

    # gets biggest ATM difference between closes instances
    def most_diff(self):
        maxdiff = 0
        pos = 0
        if len(self.__class__.instances)<2:
            print("Not enough instances to compare anything.")
        else:
            for i in range(len(self.__class__.instances)-1):
                if abs(self.__class__.instances[i].atm - self.__class__.instances[i+1].atm) > maxdiff:
                    maxdiff = abs(self.__class__.instances[i].atm - self.__class__.instances[i+1].atm)
                    pos = i
        return [self.__class__.instances[pos], self.__class__.instances[pos+1]]


date1 = "04/08/2022"
date2 = "03/08/2022"
date3 = "03/07/2022"
date4 = "21/09/2022"
x1 = Weather(date1, 25.5, 1020, "Rain")
x2 = Weather(date2, 20, 1060, "Hail")
x3 = Weather(date3, 22.5, 1040, "Fog")
x4 = Weather(date4, 27.5, 1055, "Clear")

for i in Weather.instances:
    print(i)

print()

result = x4.most_diff()
for i in result:
    print(i)
print(f'Difference: {abs(result[0].atm - result[1].atm)}')


# Задача 2. Створити клас ДАТИ з полями у закритій частіші: день (1-31), місяць (1- 12), рік (ціле число).
# Клас має конструктор, методи встановлення дня, місяця і року, методи отримання значень дня, місяця і року,
# а також два методи виведення за шаблонами: "12 лютого 2020 року" і "12.02.2020".
# Методи встановлення полів класу повинні перевіряти коректність параметрів, що задаються.
