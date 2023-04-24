def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Take input from the user
nterms = int(input("Enter the number of terms: "))

# Check if the input is valid
if nterms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(nterms):
        print(fibonacci(i))
