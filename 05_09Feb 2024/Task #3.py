# Fibonacci series and factorial

# Factorial
# n = 5
# 5!  --> 5*4*3*2*1-->120
# 4! --> 4*3*2*1 -->24
print("Factorial of a number")
number = int(input("Enter the factorial number: "))
if number < 0:
    print(f"Factorial is not defined for negative number {number}")
elif number == 0:
    print(f"Factorial of {number} = ", 1)
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    print(f"The factorial of {number} = ", fact)

# Fibonacci series
# 0, 0+1, 0+1+1
# n = 9 --> 0,1, 1, 2, 3, 5, 8, 13, 21

# Method1 using while loop
# 0,1, 1, 2, 3, 5, 8, 13, 21
a, b = 0, 1
count = 1
while count < 9:
    print(a)
    a, b = b, a + b

# Method2 using function
count = 9
n1, n2 = 0, 1
for i in range(1, count + 1):
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2


def fibonacci(count1):
    a1, a2 = 0, 1
    if count1 <= 0:
        print("Incorrect input")
    else:

        for i in range(1, count1 + 1):
            a1, a2 = a2, a1 + a2
            print("a1:", a1)
            return a1  # return will break the for loop after only one iteration. So this will not work


result = fibonacci(9)
print("Hello")
print(result)
