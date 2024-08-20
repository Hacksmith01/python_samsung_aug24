# Program to check if user given year is a Leap year.

give_year=int(input("Enter the year: "))

if give_year % 4 == 0:
    if give_year % 100 == 0:
        if give_year % 400 == 0:
            print("The given year is a leap year")
        else:
            pass
    else:
        pass
else:
    pass    
