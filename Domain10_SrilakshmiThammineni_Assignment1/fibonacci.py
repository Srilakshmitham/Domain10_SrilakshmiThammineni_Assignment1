n = int(input("Enter the number of terms: "))
a, b = 0, 1
fibonacci = []
for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b
print("Fibonacci sequence:", fibonacci)
