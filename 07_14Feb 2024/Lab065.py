# List
# List - Collection of items (Duplicate is allowed)
my_list = [1, 2, 3]
my_list2 = [1, True, "Test", 34]

# Indexing
print("Element at index 0:", my_list[0])

# Changing an element
my_list[2] = 5
print("List after changing element at index 2:", my_list)

# Append()  --add at the end
my_list.append(40)
print("List after appending:", my_list)

# extend()
my_list.extend([66,77])
print("List after extending: ", my_list)

# insert
my_list.insert(2,'a')
print("List after inserting 'a' at index 2: ", my_list)

# remove
my_list.remove('a')
print("List after removing 'a': ", my_list)

# copy
my_list_copy = my_list.copy()
print(my_list_copy)

# clear
# my_list.clear()
print("Initial list: ", my_list)
print(my_list_copy)  # copy list exists even after clear, initial list will be cleared

print("value at index 3 in the list:", my_list.index(1))  # op is 3

my_list_copy.sort()
print(my_list_copy)
my_list_copy.reverse()
print(my_list_copy)

print(my_list_copy[0])
print(my_list_copy[1])
print(my_list_copy[2])
print(my_list_copy[3])