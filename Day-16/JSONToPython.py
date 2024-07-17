import json

# some JSON:
x = '{ "name":"Rani", "age":24, "city":"Banglore"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])