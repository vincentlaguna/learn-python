# Example using the random module
import random
from time import sleep 
print("Generating random number between 1 and 100...\n")
sleep(1)
random_list = []
random_list = [random.randint(1,101) for i in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)