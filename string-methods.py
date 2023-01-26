str1 = "Hello World"
print(str1.upper())  # Convert string into upper case characters
print(str1.lower())  # Convert string into lower case characters
print(str1.capitalize())  # Capitalize the string

print('\n---------------------------------------------')
str2 = " Welcome to Python "
print(str2.strip())  # Remove starting and ending spaces
print(str2.lstrip())  # Remove left side spaces
print(str2.rstrip())  # Remove right side spaces
print(str2.count("e"))  # For counting number of any specific character

print('\n---------------------------------------------')
str3 = "12345"
str4 = "ABCD"
print(str3.isnumeric())  # Return if string consist of only numbers or not
print(str4.isnumeric())

print('\n---------------------------------------------')
print(int(str3))  # Converting a numeric string into integer
print(int(str3) + int(54321) + 123)

print('\n---------------------------------------------')
list1 = ["Hello!", "How", "are", "you", "mate?"]
str5 = " ".join(list1)  # Joining list of strings with spaces
str6 = "...".join(list1)  # Joining list of strings with ...
print(str5 + "\n" + str6)

print(str5.split())  # Splitting a string into a list of strings
