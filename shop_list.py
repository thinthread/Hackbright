my_list = []

def add_list():
	choice = raw_input("What would you like to add to the shopping list?").lower()
	if choice in my_list:
		print "You already have that item."
	else: 
		my_list.append(choice)

	my_list.sort()

def print_list():
	for item in my_list:
		print (item)

def remove_item_from_list():
	Choice_remove = raw_input ("What would you like to remove?").lower()
	if Choice_remove not in my_list:
		print "You don't have that item in the list."
	else:
		my_list.remove(Choice_remove)
	
	my_list.sort()

def menu():
	while True:
		print("0 - Main menu.")
		print("1 - Show current list.")
		print("2 - Add item to your shopping list.")
		print("3 - Remove item from shopping list.")
		print("4 - Quit the program.\n")

		menu_items = raw_input("Please choose one of the menu options: 0,1,2,3 or 4.\n")

		if menu_items == "1":
			print_list()

		elif menu_items == "2":
			add_list()

		elif menu_items == "3":
			remove_item_from_list()

		elif menu_items == "4":
			break

		else:
			print ("Choose 0,1,2,3, or 4.")

def main():
	menu()



if __name__ == '__main__':
	main()
	print