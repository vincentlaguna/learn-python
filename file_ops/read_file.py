# This will cover different ways to read files in Python
with open("test1.txt") as test_text1:
    content1 = test_text1.read()
print(content1)
# Iterate through each line
with open("test1.txt") as test_text1:
    for line in test_text1:
        print(line)
# Notice the addition of empty new-lines in the output
