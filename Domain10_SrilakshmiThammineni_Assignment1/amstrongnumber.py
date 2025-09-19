num = int(input("Enter a number: "))

# Converting number to string to get the number of digits
digits = str(num)
power = len(digits)

# Calculating the sum of digits raised to the power of the number of digits
total = sum(int(d)**power for d in digits)

# Checking if the number is an Armstrong number
print(num == total)  # Print

