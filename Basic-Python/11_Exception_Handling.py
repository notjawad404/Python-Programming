# Handling Basic Exception

num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")

try:
    num3 = int(num1) / int(num2)  # Perform division and store the result in num3
except Exception as e:
    print("Exception occurred: ", e)  # Print the exception message if an exception occurs
    num3 = None  # Set num3 to None in case of an exception

print("Answer = ", num3)  # Print the value of num3


# Handling Multiple Specific Exceptions

number1 = input("Enter Number 1: ")
number2 = input("Enter Number 2: ")

try:
    number3 = int(number1) / int(number2)  # Perform division and store the result in number3
except ZeroDivisionError as e:
    print("Division by Zero exception occurred: ", e)  # Print the ZeroDivisionError exception message if it occurs
    number3 = None  # Set number3 to None in case of ZeroDivisionError
except TypeError as e:
    print("Type Error exception occurred: ", e)  # Print the TypeError exception message if it occurs
    number3 = None  # Set number3 to None in case of TypeError

print("Answer = ", number3)  # Print the value of number3
