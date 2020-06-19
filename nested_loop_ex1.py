# Simple nested loop that prints the sum of all the elements
a = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
sum = 0

for i in a:
  print(i)
  for j in i:
    sum += j
    
print(sum)