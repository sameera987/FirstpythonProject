# Triangle classifier
# write a program that classifies  a triangle based on its side lengths
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral
# (all sides are equal), isosceles (exactly two sides are equal) or scalene (No sides are equal)
# use an if else statement to classify the triangle.
side1 = float(input("Enter the side1 : \n"))
side2 = float(input("Enter the side2 : \n "))
side3 = float(input("Enter the side1 :\n "))

if side1 == side2 == side3:
    print("The triangle is equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")


