# Fibonacci  Sequence

def fibonacci(n):
    print("F(0) : " + str(0))
    print("F(1) : " + str(1))
    for x in range(2, n+1):
        print("F("+str(x)+") : "+str(x - 1 + x - 2))


fibonacci(10)

