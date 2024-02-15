def make_pizza(*toppings):
    for topping in toppings:
        print(topping)
    # print(toppings)  # if for loop is not used


make_pizza("mushroom")
make_pizza("onion", "mushroom")


def make_pizza(*toppings, base):
    print(toppings, base)
    for topping in toppings:
        print(topping, base)


x = make_pizza("abc", "xyz", base="thin")
print(x)  # do not return anything

# def make_pizza(*toppings, *base): # multiple * parameters are not allowed
