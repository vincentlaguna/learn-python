# Return a list of every third number between start and 100 (inclusive)
print("Returning a list of every third number: \n")
def every_three_nums(start):
  return list(range(start, 101, 3))
  
print(every_three_nums(91))

# Return a list where all elements in lst with an index between
# start and end (inclusive) have been removed.
print("\nReturning a list where the middles elements have been removed: \n")
def remove_middle(lst, start, end):
  lst = lst[:start] + lst[end + 1:]
  return lst
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# Return either item1 or item2 depending on which item appears more often in lst
print("\nReturning highest element count of two lists: \n")
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Removing elements from a list
print("\n---Proceeding to eliminate even elements from this list: \n")
def delete_starting_evens(lst):
  while(len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Return odd indices
print("---Proceeding to iterate through odd indices in this list: \n")
def odd_indices(lst):
  new_lst = []
  for i in range(1, len(lst), 2):
    new_lst.append(lst[i])
  return new_lst
print(odd_indices([4, 3, 7, 10, 11, -2]))

# Return a list of exonentiated numbers of two lists
print("\nReturning an exponentiated list created from two lists: \n")
def exponents(bases, powers):
  new_lst = []
  for i in bases:
    for j in powers:
      new_lst.append(i ** j)
  return new_lst
  
print(exponents([2, 3, 4], [1, 2, 3]))