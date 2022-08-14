Year = int(input())

if Year % 4 == 0 and Year % 100 != 0:
    print(Year, "is a Leap Year")
elif Year % 100 == 0:
    print(Year, "is not a Leap Year")
elif Year % 400 == 0:
    (Year, "is a Leap Year")
else:
    print(Year, "is not a Leap Year")
