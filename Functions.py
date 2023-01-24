#-----  Functions  -----

def intro(name):
    print("Hello "+ name)

def intro1(name, location):
    print("My Name is "+ name )
    print("I am from "+ location)

intro("Alex")
intro1("Alex", "London")

#----- Returning Values -----

def area_triangle(height, length):
    return height*length/2

area_a = area_triangle(4,7)
area_b = area_triangle(6,9)

sum = area_a + area_b
print("Sum of 2 triangles is : "+str(sum))