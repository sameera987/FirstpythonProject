def make_pizza(*toppings, base="wheat"):
    print(toppings, base)
    for topping in toppings:
        print(topping)
        return toppings, base


x, y = make_pizza("Test1", "Test2", base='base')

print(x)
print(y)
