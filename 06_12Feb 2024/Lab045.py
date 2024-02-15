# pass
# skip the code
for i in range(1, 10):
    if i == 5:
        pass
    else:
        print(i)
# o/p: 1,2,3,4,6,7,8,9

for i in range(1, 10):
    if i == 5:
        break
    else:
        print(i)
# op: 1,2,3,4