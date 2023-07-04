# Function to calculate the product of all numbers within a given range

def product1(p1):
    product = 1  # Initialize the product variable to 1
    for n in range(1, p1 + 1):  # Iterate over the range from 1 to p1 (inclusive)
        product = product * n  # Multiply the current number with the product

    print(product)  # Print the final product

product1(5)  # Calling the product1 function with argument 5
