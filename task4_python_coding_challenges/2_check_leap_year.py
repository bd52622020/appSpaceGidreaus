import calendar

def check_leap_year(year):
    if calendar.isleap(year):
        print(year, " is a leap year.")
    else:
        print(year, " is not a leap year.")

print("\nQ2")         
check_leap_year(1990)
check_leap_year(2000)   


