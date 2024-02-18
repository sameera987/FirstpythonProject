# To reverse a string

name = input("Enter a name")  # naman
reverse = ""
# print(len(name) - 1)
# print(len(name))
for i in range(len(name) - 1, -1, -1):
    reverse = reverse + name[i]
print(reverse)
