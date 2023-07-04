# Fibonacci Sequence

def fibonacci(n):
    print("F(0) : " + str(0))  # Print the first Fibonacci number, F(0), which is 0
    print("F(1) : " + str(1))  # Print the second Fibonacci number, F(1), which is 1
    for x in range(2, n+1):
        # Calculate and print the Fibonacci numbers from F(2) to F(n)
        # Each Fibonacci number is the sum of the two previous Fibonacci numbers
        # F(x) = F(x-1) + F(x-2)
        print("F(" + str(x) + ") : " + str(x - 1 + x - 2))

fibonacci(10)  # Calling the fibonacci function with argument 10
