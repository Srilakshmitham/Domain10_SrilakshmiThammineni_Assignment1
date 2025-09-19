n = int(input("Enter a number: "))

factorial = 1

# Factorial of 0 or 1 is 1
for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is:", factorial)
