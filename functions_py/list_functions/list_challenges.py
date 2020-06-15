# Return a list of every third number between start and 100 (inclusive)
def every_three_nums(start):
  return list(range(start, 101, 3))
  
print(every_three_nums(91))

# Return a list where all elements in lst with an index between
# start and end (inclusive) have been removed.
def remove_middle(lst, start, end):
  lst = lst[:start] + lst[end + 1:]
  return lst
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# Return either item1 or item2 depending on which item appears more often in lst
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))