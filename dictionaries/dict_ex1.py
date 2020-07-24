# Examples of using dictionaries in Python
print("Quick example of using a dictionary in Python: ")
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# Changing Values in dictionaries
print("\nChanging a value in a dictionary: ")
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
print("Modifying values in dictionary...")
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

# Using list comprehension inside a dictionary
print("\nUsing list comprehensions in a dictionary: ")
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks)
print(caffeine)
print("Using list comprehension for both lists...")
print(drinks_to_caffeine)

# Review challenge
print("\nReview challenge: ")
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1

plays.update({"Respect": 94})

library = {"The Best Songs": plays, "Sunday Feelings": ""}

print("Updating lists into dictionary...")
print(library)

library.update({"Sunday Feelings": {"Everyday is like Sunday": 99}})

print("Updating Library dictionary...")
print(library)

# Example of using .get() and modifying non-existent values
print("\nExample of using .get() and modifying non-existent key-values in a dictionary: ")

tc_id = user_ids.get("teraCoder", 1000)
print("Returning TeraCoder's id -> ")
print(tc_id)

print("Returning superStackSmash's id (auto-assigning is non-existent) -> ")
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# Example of getting a key and removing it from the dictionary afterwards:
print("\nExample of getting and assigning a key value and then removing it from the dictionary -> ")
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

# Example of getting all the dictionary key objects:
print("\nExample of getting all the dictionary key objects using .keys()")
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
print(list(users))
print(list(lessons))

print("\nIterating and assinging the sum of values -> ")
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22,
                 "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0

for i in num_exercises.values():
  total_exercises += i

print(total_exercises)

# Example of iterating and using .items:
print("\nExample of iterating using .items() to list the output properly ->")
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for i, v in pct_women_in_occupation.items():
  print("Women make up " + str(v) + " percent of " + i + "s.")
  
print("\nDictionary review exercise -> ")
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for i, value in spread.items():
  print("Your " + i + " is the " + value + " card.")
  
# Iterating through a dictionary where values are also keys:
print("\nExample of diplaying on the the keys that are also values in a dictionary ->")
print("{1:100, 2:1, 3:4, 4:10}, {a:apple, b:a, c:100}")
def values_that_are_keys(my_dictionary):
  key_values = []
  for i in my_dictionary.values():
    if i in my_dictionary:
      key_values.append(i)
  return key_values

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))