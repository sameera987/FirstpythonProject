mylist = []
for i in range(10):  # ---0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    mylist.append(-1)
print(mylist)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mylist[n] != -1:
        return mylist[n]
    mylist[n] = fib(n - 1) + fib(n - 2)
    return mylist[n]


num = 10
for i in range(num):
    print(fib(i), end=" ")
