
year = int(input("Enter a year: "))

# Checking leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)   # Leap year
else:
    print(False)  # Not a leap year
