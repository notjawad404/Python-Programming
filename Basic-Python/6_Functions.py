#----- Functions -----

# Function to greet a person by name
def intro(name):
    print("Hello " + name)

# Function to introduce a person with name and location
def intro1(name, location):
    print("My Name is " + name)
    print("I am from " + location)

intro("Alex")  # Calling intro function with argument "Alex"
intro1("Alex", "London")  # Calling intro1 function with arguments "Alex" and "London"

#----- Returning Values -----

# Function to calculate the area of a triangle
def area_triangle(height, length):
    return height * length / 2

area_a = area_triangle(4, 7)  # Calling area_triangle function and storing the result in area_a
area_b = area_triangle(6, 9)  # Calling area_triangle function and storing the result in area_b

sum = area_a + area_b  # Calculating the sum of the areas of the two triangles
print("Sum of 2 triangles is : " + str(sum))  # Printing the sum
