# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
list = [{"name": "Raghu", "age": 20},
	{"name": "Bharath", "age": 20},
	{"name": "AbhiRam", "age": 19}]

print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))

print("\r")

print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))

print("\r")

print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))
