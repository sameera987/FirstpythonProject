# Conditions
# age > 18 -> allowed to vote
# age < 18 -> you are not allowed

age = int(input("Enter your age"))
if age > 18:
    print("Allowed to vote")
else:
    print("Not allowed to vote")

    # if condition  -->return True or False
a = 5
# if a=5: --> this will not return the condition True or False
if a == 5:
    print("true")
else:
    print("false")

x = 10
y = 20
# x > y
# x < y
# x ==y
if x > y:
    print("x > y")
elif x < y:
    print("x < y")
else:
    print("x and y are equal")
