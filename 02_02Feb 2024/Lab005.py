# Predefined functions (print(), max())

# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print

# values are arguments. default separator is space
print("test1", 'test2', "test3")
# user defined seperator $
print("test1", 'test2', "test3", sep='$')

# default separator is \n (new line)
print("Test1", 'Test2', "Test3")
print("Test1", 'Test2', "Test3")

# user defined separator
print("Test1", 'Test2', "Test3", end='#')
print("Test1", 'Test2', "Test3")

x = str(max(4, 5, 6))
print(x)
print(type(x))
