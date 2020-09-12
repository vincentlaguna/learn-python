# This will cover different ways to read files in Python
print("Reading the entire file using read(): \n")
with open("test1.txt") as test_text1:
    content1 = test_text1.read()
print(content1)

# Iterate through each line
print("\nIterating through each line using a for loop: \n")
with open("test1.txt") as test_text1:
    for line in test_text1:
        print(line)
# Notice the addition of empty new-lines in the output

# To read a specific line i.e. second line in the file
print("\nUsing readline() to only read the second line in the file: \n")
with open("test1.txt") as test_text1:
    first_line = test_text1.readline()
    second_line = test_text1.readline()
print(second_line)

# Create and write to a file
print("Generating and writing to a file...\n")
with open("python_generated_file1.txt", "w") as gen_file1:
    gen_file1.write("This is a python generated file, Hello World!\n")
# Read the contents of the generated file
print("Reading the python-generated file: \n")
with open("python_generated_file1.txt", "r") as read_gen_file1:
    r_gen_file1 = read_gen_file1.read()
print(r_gen_file1)