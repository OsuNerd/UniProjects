# Задача 1. Розробити клас з даними про ПОГОДУ: дата, середня температура, атмосферний тиск, опади.
# Визначити конструктори, методи / властивості встановлення та читання значень полів даних.
# Визначити дні з найбільшим перепадом тиску.
from datetime import datetime

class Weather:
    instances = []

    # Date must be in form of string *-*-*
    def __init__(self, date: str, avg_temp: float, atm: float, precipitation: str):
        self.date = date
        self.avg_temp = avg_temp
        self.atm = atm
        self.__precipitation = precipitation

        self.save()

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self.__date = (datetime.strptime(date, "%d-%m-%Y")).date()
        else:
            raise ValueError("Wrong datatype for date.")

    @property
    def avg_temp(self):
        return self.__avg_temp

    @avg_temp.setter
    def avg_temp(self, avg_temp: float):
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


date1 = "04-08-2022"
date2 = "03-08-2022"
date3 = "03-07-2022"
date4 = "21-09-2022"
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

# січень, лютий, березень, квітень, травень, червень, липень, серпень,вересень, жовтень, листопад, грудень.

class Data:
    moninfo = {1: ["січня", 31], 2: ["лютого", 28], 3: ["березеня", 31], 4: ["квітня", 30], 5: ["травня", 31],
               6: ["червня", 30], 7: ["липня", 31], 8: ["серпня", 31], 9: ["вересня", 30], 10: ["жовтня", 31],
               11: ["листопада", 30], 12: ["грудня", 31]}

    def __init__(self, day: int, month: int, year: int):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise ValueError("Value type is not correct. All attributes must be int.")
        self.year = year
        self.month = month
        self.day = day
        self.__leap_year: bool

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    @year.setter
    def year(self, year):
        if year < 0:
            raise ValueError("Year can't be a negative number.")
        if year % 4 == 0:
            if year % 100 != 0:
                self.__year = year
                self.__leap_year = True
            elif year % 400 == 0:
                self.__year = year
                self.__leap_year = True
            else:
                self.__year = year
                self.__leap_year = False
        else:
            self.__year = year
            self.__leap_year = False

    @month.setter
    def month(self, month):
        if 0 < month < 13:
            self.__month = month
        else:
            raise ValueError("Month value cannot be lower than 0 or higher than 12.")

    @day.setter
    def day(self, day):
        if self.__leap_year and (self.__month == 2):
            if 0 >= day or day > self.__class__.moninfo[self.__month][1]+1:
                raise ValueError("Value for day is either less than 1 or doesn't exist in current month.")
            self.__day = day
        elif 0 >= day or day > self.__class__.moninfo[self.__month][1]:
            raise ValueError("Value for day is either less than 1 or doesn't exist in current month.")
        self.__day = day

    def output_words(self):
        print(f'{self.__day} {self.__class__.moninfo[self.__month][0]} {self.__year} року')

    def output_num(self):
        print(f'{self.__day:02d}.{self.__month:02d}.{self.__year}')


x1 = [Data(4, 8, 2022), Data(3, 8, 2022), Data(28, 2, 2022), Data(27, 2, 2022), Data(29, 2, 2024), Data(6, 1, 1990)]

for i in x1:
    i.output_words()
    i.output_num()

# x2 = Data(29, 2, 2022)  # raises exception because of date
# x3 = Data(25, 0, 2022)  # raises exception because of month
# x4 = Data(20, 4, -1)  # raises exception because of year
