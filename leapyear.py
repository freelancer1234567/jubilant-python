#leap year
def daysInYear(year):
       if(year%4==0):
        print("it is a leap year and it has 366 days")
       else:
        print("it is not a leap year and it has 365 days")
year=int(input("enter a year:"))
daysInYear(year)
