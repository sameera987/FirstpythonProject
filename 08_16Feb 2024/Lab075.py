# Tuple - Collection of items
# List - Collection of items
# List are mutable, we can change
my_list = [1, 2, 3, 4, 5]
my_list[0] = 21
print(type(my_list))

# Tuple
my_tuple = (1,2,3,4,5)
# my_tuple[0] = 20 # TypeError: 'tuple' object does not support item assignment
print(type(my_tuple))
print(len(my_tuple))

new_tup = tuple(my_list)
print(new_tup)