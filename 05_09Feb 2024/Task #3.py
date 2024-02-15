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
# n = 7 --> 0,1, 1, 2, 3, 5, 8, 13
