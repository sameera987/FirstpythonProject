# Dictionary - is an unordered collection of data in a key-value pair
# key and value
name = "sam"  # Normal string
# key --> name
# value --> "sam"

my_dict = {}
my_dict2 = dict()

print(type(my_dict))  # <class 'dict'>
print(type(my_dict2))  # <class 'dict'>

# dictionary example
phone_book = {"batsman": 123456789, "Superman": 987654321, "Wonder": 123456}
print(len(phone_book))
print(phone_book["batsman"])

phone_book2 = dict(Batman=123, Cersei=10)
print(phone_book2)
print(phone_book2["Batman"])
print(phone_book2["Cersei"])

test_details = dict(name="test", age=30, isMale=True, Address="Add")
test_details2 = {"name": "test", "age": 30, "isMale": True, "Address": "Add"}
print(test_details2.get("age"))

my_dict3 = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(len(my_dict3))
print(my_dict3)