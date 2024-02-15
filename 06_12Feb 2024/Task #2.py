# Implement a Function to Calculate the Factorial of a Number

def factor(num):
    if num >= 0:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact
    else:
        print(f"Factorial is not defined for negative number, {num}")


# print("return value", factor(-2))  # To check if function is returning correct factorial
number = int(input("Enter the factorial number: "))
Factorial = factor(number)
print(Factorial)
