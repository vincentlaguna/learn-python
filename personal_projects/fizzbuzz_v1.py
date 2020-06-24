# First try at Fizz Buzz in Python
lst = range(1, 101)
print(list(lst))

def fizz_buzz(list):
  for i in list:
    if (i % 5 == 0) and (i % 3 == 0):
      print("FizzBuzz!")
    elif (i % 3 == 0):
      print("Fizz")
    else:
      print(i)

fizz_buzz(lst)
