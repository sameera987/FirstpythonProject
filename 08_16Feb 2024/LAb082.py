t = ("Test1", "Test1", "for")
print(set(t))  # op: {'for', 'Test1'}

set1 = {1, 2, 5}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)
my_set1 = set1.intersection(set2)
print(my_set1)
my_set2 = set1.difference(set2)
print(my_set2)

