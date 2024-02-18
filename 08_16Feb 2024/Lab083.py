set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
subset1 = set1.issubset(set2)
subset2 = set2.issubset(set1)
print(subset1)  # False
print(subset2)  # True

my_set = set(["test1", "test2", "test2.", "For"])
print(my_set) # {'test2', 'test2.', 'For', 'test1'}

for i in my_set:
    print(i)

set3 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print(set3)
print(len(set3))
set3.remove(3)
set3.remove(12)
print(len(set3))