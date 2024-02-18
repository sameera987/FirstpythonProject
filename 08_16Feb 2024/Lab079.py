x = 10
a, b = 2, 3
p, q, r = (1, 2, 3)

# Nested tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Women", "Diana Princess")
result = (hero1, hero2)  # (('Batman', 'Bruce Wayne'), ('Wonder Women', 'Diana Princess'))
print(result)
print(result[0])  # ('Batman', 'Bruce Wayne')
print(result[1])  # ('Wonder Women', 'Diana Princess')
print(result[0][0])  # Batman
print(result[0][1])  # Bruce Wayne
print(result[1][0])  # Wonder Women
print(result[1][1])  # Diana Princess

# Search in tuple
items = ("London", "Paris", "Tokyo")
items = ("London", "Paris", "Tokyo")
print("Paris" in items)  # true
print("PariS" in items)  # False


