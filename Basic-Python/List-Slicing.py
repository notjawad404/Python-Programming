# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

#Get the last element
last = areas[-1]
print(last)

#Get a specific element
element = areas[3]
print(element)

# Slicing middle elements
middle = areas[2:6]
print(middle)

# Slicing to create downstairs
downstairs = areas[:6]

# Slicing to create upstairs
upstairs = areas[6:]

print(downstairs,'\n',upstairs)
