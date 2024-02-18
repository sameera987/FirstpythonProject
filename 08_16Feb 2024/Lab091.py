# Dict i smutable
# can be directly used in json
api_response = {
    "age": 34,
    "last_name": "Last name",
    "first_name": "First name",
    "email_id": "unitedemail@live.com",
    "password": "Test@9876"}

print(api_response)
print(type(api_response))
print(api_response.get('password'))

for key, value in api_response.items():
    print(key, "=>",  value)

api_response["password"] = "Test"
print(api_response)