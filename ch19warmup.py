# my_tuple = ("Jasmin", "Herrera")
# my_list = sorted(list(my_tuple), reverse = False)
# print my_list


# for number in range(1000, 0, -100):
# 	print number

import random

three_names = ["Steven", "Michael", "James"]

# for names in range():

# 	print(random.choice(three_names))

new_name = []

while len(new_name) <2:
	new_name.append(random.choice(three_names))

print ' '.join(new_name)