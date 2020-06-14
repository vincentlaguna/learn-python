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