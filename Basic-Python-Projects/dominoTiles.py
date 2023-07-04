# Code for generating tiles combinations

def tiles():
    for left in range(7):
        for right in range(left, 7):
            print("[" + str(left) + "|" + str(right) + "]", end=" ")  # Print the left and right values inside brackets
        print("\n")  # Print a new line after each iteration of the inner loop

tiles()  # Calling the tiles function
