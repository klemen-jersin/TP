import json

# a Python object (dict):
podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(podatki)

# the result is a JSON string:
print(y)
print(type(y))