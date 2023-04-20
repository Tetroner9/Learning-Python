def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


terms = int(input("Enter no. of terms: "))
while True:
    terms = int(input("Enter a positive integer: "))
    if terms <= 0:
        print("Invalid input, please enter a positive integer!")
    else:
        print("Fibonacci series: ")
        for i in range(terms):
            print(fibo(i))
        break
