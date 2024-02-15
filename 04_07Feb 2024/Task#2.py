# write a program to calculate the area of a circle, given its radius  using the formula  area = pi*r*r (pi = 3.14).
# Take r from user as float
import math
#Method 1
π = 3.14
radius = float(input("Enter the radius of the circle in cm: "))
area_of_circle = π * radius * radius
print(f"Area of the circle is = {area_of_circle} sq.cm")
#Method 2
radius1 = float(input("Enter the radius of the circle1: "))
area_of_circle1 = math.pi * radius1**2
print("Area of the circle is: ", area_of_circle1)


# Create a program  that takes two numbers  as input  and prints  whether the first number  is greater than,
# less than  or equal to  the second number (dot use if loop, use only operator, <,>)
#Method 1 using operators
a = 10
b = 20
print(a==b)  # O/P is False
print(a>b)   # O/P is False
print(a<b)   # O/P is True

number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
print("Both the numbers are equal: ", number1 == number2 )
print("First number is greater than second number: ", number1 > number2 )
print("First number is less than second number: ", number1 < number2 )



#Method 2 using if loop
number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
if number1  >  number2:
    print("number1 is greater than number2")
elif number1  <  number2:
    print("number1 is less than number2")
else:
    print("number1 is equal to number2")


# Develop a python script  that calculates the square and cube  of a given number
#Method 1:
number = int(input("Enter the number: "))
srq_of_number =  number**2
print("Square of number:", srq_of_number)
cube_of_number = number**3
print("Cube of number:", cube_of_number)

#Method 2:
print(f"Square of {number} is {srq_of_number}\n cube of {number}  is {cube_of_number}")
