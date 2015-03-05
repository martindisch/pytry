# Checks for leap-years

while 1:
    year = input("What's the year? ")
    
    if year == 0:
        break
    
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("You got yourself a leap-year!")
    else:
        print("No luck with that...")

print "\nPlease come again!\n"
