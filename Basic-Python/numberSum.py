# Program to print the sum of numbers from 0 to a given number
# Using While Loop

def numSum(n):
    x = 0
    sum1 = 0
    while x <= n:
        sum1 = sum1 + x  # Add the current number (x) to the sum
        x = x + 1  # Increment x by 1 for the next iteration
    print(str(sum1))  # Print the final sum

numSum(100)  # Calling the numSum function with argument 100


# Using For Loop

def numSum1(num1):
    sum1 = 0
    for x in range(num1):
        sum1 = sum1 + x  # Add the current number (x) to the sum
    print(sum1)  # Print the final sum

numSum1(100)  # Calling the numSum1 function with argument 100
