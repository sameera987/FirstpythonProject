# map()
def sq_of_number(num):
    return num ** 2


result = sq_of_number(10)
print(result)


def sq_of_number1(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]
# use Map()
# Takes each item from list
# Execute the function on it
# Return the same number of elements(list)
sq_numbers = list(map(sq_of_number1,numbers))
print(sq_numbers)
