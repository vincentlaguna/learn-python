# Append items to a list by checking its value
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp",
"@matchamom", "follow", "#updog"]

usernames = []

for i in words:
  if i[0] == "@":
    usernames.append(i)
    
print("Usernames -> " + str(usernames)) # type-cast list to string
# Short=hand version:
non_usernames = [i for i in words if i[0] != "@"]
print("Non-Usernames -> " + str(non_usernames)) # type-cast list to string