def leap_year(year):
    return year % 4 == 0 if year % 100 != 0 else year % 400 == 0

print(leap_year(2000))