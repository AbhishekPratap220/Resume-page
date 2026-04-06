year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"Leap Year")
else:
    print(year,"Not Leap Year")