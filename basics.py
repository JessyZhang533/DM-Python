# Infinite while loop: while True; need to break when a condition is true
while True:
    username = input("Enter your name: ")  # Take input from user (user types in terminal)
    if username == "Jessy":
        print("Welcome, {}".format(username))
        break
    else:
        print("Wrong name")

# Logical operators
print(20 < 3 and 1 < 3)
print(20 < 3 or 1 < 3)
print(not 20 < 3)

# Divisions
print(4 / 2)  # Float division; result must be a float
print(5 // 2)  # Integer division; result must be an integer
print(5 % 2)  # Modulo; result must be an integer

# Dictionary
people_age = {"Anna": 18, "James": 7, "Lisa": 31}
for i in people_age:  # Here i denotes the keys
    print(i)
for i, j in people_age.items():  # Here i denotes the keys, j denotes the values
    print(i, j)

# Enumerate https://www.programiz.com/python-programming/methods/built-in/enumerate
my_list = [1, 3., 67]  # Also applicable to tuples
print(type(enumerate(my_list)))  # This is an enumerate object
print(list(enumerate(my_list)))  # Convert to a list to view

# Differences between lists and tuples https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/
