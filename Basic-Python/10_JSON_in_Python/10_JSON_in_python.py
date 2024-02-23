import json

# Create a dictionary to store information about people
person = {}

# Add information for person A
person['A'] = {
    "name": "John Price",
    "address": "ABC 12 AC",
    "phone_number": 1213232334256
}

# Add information for person B
person['B'] = {
    "name": "Simon Riely",
    "address": "2 Grove Street LA",
    "phone_number": 1213232334256
}

# Convert the person dictionary to a JSON string
str = json.dumps(person)

# Write the JSON string to a file
with open('person.txt', 'w') as file:
    file.write(str)
    
# Read the contents of the file
file = open('person.txt', 'r')
str1 = file.read()

# Print the contents of the file
print(str1)

# Convert the JSON string back to a dictionary
person1 = json.loads(str)

# Print the dictionary
print(person1,"\n")

# Print the information of person B
print(person["B"],"\n")

# Print the phone number of person A
print(person["A"]['phone_number'],"\n")

# Iterate over each person in the dictionary and print their information
for p in person:
    print(person[p])
