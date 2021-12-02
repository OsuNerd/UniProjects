import datetime

day, month, year = int(input('Day of Birth = ')),\
                   int(input('Month of Birth = ')),\
                   int(input('Year of Birth = '))

date_of_birth = datetime.date(year, month, day)

today = datetime.date.today()

age_days = (today - date_of_birth).days

age = age_days // 365

print('Your age is', age)
