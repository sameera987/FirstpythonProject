# Filter
# It can filter the items from the list based on the logic
# return less number of items

number = [1, 2, 3, 4, 5, 6]
# using lambda function
even_numbers = filter(lambda item: item % 2 == 0, number)
print(list(even_numbers))


# using function
def even(num):
    return num % 2 == 0


even_num = filter(even, number)
print(list(even_num))
