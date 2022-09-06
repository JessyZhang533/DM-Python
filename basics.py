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
