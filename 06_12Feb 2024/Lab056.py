def sum_of_numbers(a, b):
     return a+b

result = sum_of_numbers(3, 7)
print(result)

result = sum_of_numbers(1, -3)
print(result)

result = sum_of_numbers("Test1 ", "Test2")
print(result)

result = sum_of_numbers(3, "Test2")
print(result)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'