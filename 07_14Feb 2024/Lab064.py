# Lambda expression
# To help us
# f(n) --> one liner in python
def say_hello():
    print("Hello")


say_hello()


def sal_test(salary):
    # final_sal = salary * 2
    #    return final_sal
    return salary * 2


result = sal_test(10000)
print(result)

x = lambda salary1: salary1 * 2
print(x(100))

pow_of_two = lambda num: num ** 2
print(pow_of_two(5))

sum1 = lambda a, b, c: a + b + c
print(sum1(1,2,3))

say_my_name = lambda name: print("Your name is", name)
say_my_name("sample")

