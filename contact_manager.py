from Contact import Contact 

#1
contact_list = [Contact("Talia"), Contact("Stephanie")]

#2
def new_contact():
	new_first = raw_input("What is the first name of your contact? ")
	new_last = raw_input("What is the last name of your contact? ")
	new_mobile = raw_input("What is their mobile number? ")
	new_work_number = raw_input("What is their work number? ")
	new_email = raw_input("What is their email? ")
	new_twitter= raw_input("What is their twitter handle? ")
	contact_info = Contact (new_first, last_name = new_last, mobile = new_mobile, work_number = new_work_number, email = new_email, twitter_handle = new_twitter)
	contact_list.append(contact_info)
#3	
def show_contacts():
	for info in contact_list:
		print info.first_name, info.last_name, info.mobile, info.work_number, info.email, info.twitter_handle
#4
def check(contact_chosen):
	for contact in contact_list:
		if contact.first_name == contact_chosen:
			return contact
	return None
#5
def edit_part(contact_chosen, part_change, new_info, contact):
	if part_change == "first name":
		for i in range(len(contact_list)):
			if contact_list[i].first_name == contact_chosen:
				contact_list[i].first_name = new_info
				print "Your new contact is:", contact_list[i].first_name, contact_list[i].last_name, contact_list[i].mobile, contact_list[i].work_number, contact_list[i].email, contact_list[i].twitter_handle
	elif part_change == "last name":
		for i in range(len(contact_list)):
			if contact_list[i].first_name == contact_chosen:
				contact_list[i].last_name = new_info
				print "Your new contact is:", contact_list[i].first_name, contact_list[i].last_name, contact_list[i].mobile, contact_list[i].work_number, contact_list[i].email, contact_list[i].twitter_handle
	elif part_change == "mobile":
		for i in range(len(contact_list)):
			if contact_list[i].first_name == contact_chosen:
				contact_list[i].mobile = new_info
				print "Your new contact is:", contact_list[i].first_name, contact_list[i].last_name, contact_list[i].mobile, contact_list[i].work_number, contact_list[i].email, contact_list[i].twitter_handle
	elif part_change == "work number":
		for i in range(len(contact_list)):
			if contact_list[i].first_name == contact_chosen:
				contact_list[i].work_number = new_info
				print "Your new contact is:", contact_list[i].first_name, contact_list[i].last_name, contact_list[i].mobile, contact_list[i].work_number, contact_list[i].email, contact_list[i].twitter_handle
	elif part_change == "email":
		for i in range(len(contact_list)):
			if contact_list[i].first_name == contact_chosen:
				contact_list[i].email = new_info
				print "Your new contact is:", contact_list[i].first_name, contact_list[i].last_name, contact_list[i].mobile, contact_list[i].work_number, contact_list[i].email, contact_list[i].twitter_handle
	elif part_change == "twitter handle":
		for i in range(len(contact_list)):
			if contact_list[i].first_name == contact_chosen:
				contact_list[i].twitter_handle = new_info
				print "Your new contact is:", contact_list[i].first_name, contact_list[i].last_name, contact_list[i].mobile, contact_list[i].work_number, contact_list[i].email, contact_list[i].twitter_handle
	else:
		print "That is not a part of the contact."
#6
def edit_existing_contact():
	show_contacts()
	contact_chosen = raw_input("What is the first name of the contact you'd like to edit? ")
	part_change = raw_input("Which aspect of the contact would you like to change? ")
	contact = check(contact_chosen)
	if not contact:
		print "Your contact does not exist. "
	else:
		new_info = raw_input("What would you like the contact's new " + part_change + " to be? ")
		edit_part(contact_chosen, part_change, new_info, contact)
#7
def delete_contact():
	print "Your contacts are:"
	for item in contact_list:
		print item.first_name
	contact_chosen = raw_input("Which contact would you like to delete? ")
	if check(contact_chosen) == None:
		print "Your contact does not exist."
	for i in range(len(contact_list)):
		if contact_list[i].first_name == contact_chosen:
			contact_list.remove(contact_list[i])
			break
		
def main():
	#1
	# contact_list = []
	#2
	#new_contact()
	#6
	# edit_existing_contact()
	delete_contact()
	for item in contact_list:
		print item.first_name


if __name__ == '__main__':
	main()