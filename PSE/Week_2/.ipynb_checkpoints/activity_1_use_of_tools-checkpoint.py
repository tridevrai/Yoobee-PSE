# Activity 1: 
# Write a code to use round , abs and square functions to calculate the area of a rectangle 
# and try to use both Jupyter Notebook and Py

def area_of_rectangle(length, width):
    return length * width

def square(number):
    return number**2

# initial values
length = 10.12
breadth = -20.12

# sanitize the inputs
length = round(length)
breadth = abs(breadth)

area = area_of_rectangle(length, breadth)

# print the result
print(f"The area of the rectangle is {area:.3f}")

# print the square of the area
print(f"The square of the area is {square(area):.3f}")




