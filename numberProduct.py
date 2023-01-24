# Product of all numbers within thr range

def product1(p1):
    product = 1
    for n in range(1, p1 + 1):
        product = product * n

    print(product)


product1(5)
