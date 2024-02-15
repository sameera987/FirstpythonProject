# string Concat
str1 = "Hello"
str2 = "Test"
str3 = str1 + str2
print(str3)

name = "test"
age = 20
# r = name + age
# print(r)  # TypeError: can only concatenate str (not "int") to str
r = name + str(age)
print(r)

g = "hello"
g += "Test"
g = g + "Test"
print(g)

# Increment  and Decrement ++, --
x = 5
x -= 1  # x=x-1
print(x)



