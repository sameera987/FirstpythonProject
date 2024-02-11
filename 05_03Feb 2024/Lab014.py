#Strings -->bunch of chars
# Represented by "" or ''
name = "Test1"
name2 = 'Test2'
print(type(name))
print(type(name2))
print("********************")

dir1 = "C://text.txt"
print("dir: ", dir1)
dir2 = 'C://text.txt'
print("dir2: ", dir2)
#\a has special meaning in python.so it is not printed. In this case use \\a
dir3 = 'c:\acb\abc.txt'
print(dir3)
dir4 = "c:\abc\abc.txt"
print(dir4)

#use \\
dir5 = 'c:\\acb\\abc.txt'
print(dir5)
dir6 = "c:\\abc\\abc.txt"
print(dir6)
print("********************")

# when space is present
dir7 = "C:\nome\nome test"
print(dir7)
dir8 = "C:\nome\nome test"
print(dir8)
print("********************")

print("Raw string")
#raw string concept. This will be helpful in the directory path. When special chars are present, to make it normal chars
dir9 = r"C:\nome\nome test"
print("dir9: ", dir9)

print("********************")
#format string
print("format string")
s = "Test"
print(f"Your name is {s}.")
first_name = 'FN'
last_name = 'LN'
age = '30'
is_married = 'True'
print(f"Your name is {first_name}{last_name}. Your age is {age} and you are married {is_married}")
