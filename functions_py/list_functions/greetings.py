# Append Hello to greetings
def  add_greetings(names):
  lst = []
  
  for i in names:
    lst.append("Hello, " + i)
  return lst
  
print(add_greetings(["Owen", "Max", "Sophie"]))