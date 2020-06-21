# Append items to a list by checking its value

print("\nFilter usernames from non-usernames with a conditional inside the loop: \n")
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp",
"@matchamom", "follow", "#updog"]

usernames = []

for i in words:
  if i[0] == "@":
    usernames.append(i)
    
print("Usernames -> " + str(usernames)) # type-cast list to string

# Short=hand version:
non_usernames = [i for i in words if i[0] != "@"]
print("Non-Usernames -> " + str(non_usernames) + "\n") # type-cast list to string

# Convert a list of temperatures in celsius to fahrenheit:
print("Convert a list of temperatures in celsius to fahrenheit: ")
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [i * 9/5 + 32 for i in celsius]
print("\n" + str(fahrenheit) + "\n")

# List comprehension exercise with integers:
single_digits = range(10)
print(list(range(10)))
squares = []
for i in single_digits:
  print(i)
  squares.append(i * i)
  print(squares)
cubes = [i ** 3 for i in single_digits]
print("\n" + str(cubes))