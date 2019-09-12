def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

sundays = 0
day = 366
year = 1901
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while year < 2001:
    for month in range(12):
        if day % 7 == 0:
            sundays += 1
        if month == 1 and isLeapYear(year):
            day += 29
        else:
            day += days[month]
    year += 1
print(sundays)
