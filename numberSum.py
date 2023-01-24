# Program to print the sum of the numbers from 0 to 100 or any given number
# Using While Loop
def numSum(n):
    x = 0
    sum1 = 0
    while x <= n:
        sum1 = sum1 + x
        x = x + 1
    print(str(sum1))


numSum(100)


# Using For Loop

def numSum1(num1):
    sum1 = 0
    for x in range(num1):
        sum1 = sum1 + x
    print(sum1)


numSum1(100)
