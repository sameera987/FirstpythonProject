# *args and **Kargs

def f(a=8, b=9, c=10):
    return a + b + c


# f(1)  # f() missing 2 required positional arguments: 'b' and 'c'
x = f(1, 2, 3)
y = f(a=1, b=2, c=3)
z = f()
print(x)
print(y)
print(z)


# * args
def sum1(a, b, c):  # to increase number of args, we have to manually add args in fun def
    return a + b + c


r = sum1(1, 2, 3)
print(r)


# multiple args
def p_args(*args):
    for i in args:
        print(i, end=" ")


p_args(1)
p_args(1, 3)
p_args(1, 2, 3)
p_args(1, 2, 3, 4)
