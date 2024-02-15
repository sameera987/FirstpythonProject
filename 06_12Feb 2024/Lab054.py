# 2. Non-Return type of function

# define the fun()
def greet():
    print("Hello")


# call the function
# greet()

print("*********")
for i in range(5):
    greet()
    if i == 2:
        break

print("*********")
result1 = greet()
print(result1)
