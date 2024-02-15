# Functions
# Block of code - which can be executed
# They can return something
# They can't return  --> non-return
# They have parameters
# They don't have parameters / arguments
# Define --> call
def say_hello():  # Non return type and No parameter/Argument
    print("Hello")  # Write the code


say_hello()


def say_hello_arg(name):  # Non-return type and with Argument
    print("Hello", name)  # Write the code


say_hello_arg("Test")


def say_hello_args(name, age):  # Non-return type and with multiple Argument
    print("Hello", name, age)  # Write the code


say_hello_args("Test", 66)
say_hello_args("Test", True)


def say_hello_arg_default(name="Default"):  # Non-return type and with default argument
    print("Hello", name)  # Write the code


say_hello_arg_default()
say_hello_arg_default(name="Sam1")
say_hello_arg_default("Sam")


def sum_number_arg_ret(a, b):  # return type and with argument
    return a + b


result = sum_number_arg_ret(2, 3)
result2 = sum_number_arg_ret("Test1", "Test2")
result3 = sum_number_arg_ret(a=7, b=6)


print(result)
print(result2)
print(result3)
