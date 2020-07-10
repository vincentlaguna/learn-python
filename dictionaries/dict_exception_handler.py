caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

print("Checking dictionary for matcha's caffeine level...")

try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

print("Adding matcha caffeine level to the list: ")
caffeine_level["matcha"] = 30

print("Checking dictionary again for matcha's caffeine level...")

try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")