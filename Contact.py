class Contact(object):
	def __init__ (self, first_name, last_name = "", mobile = "", work_number = "", email = "", twitter_handle = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile = mobile
		self.work_number = work_number
		self.email = email 
		self.twitter_handle = twitter_handle
	def send_text(self, message):
		if self.mobile == "":
			print "You have not set a mobile number."
		else:
			print "To: %s - %s" % (self.mobile, message)

def main():
	contact_list = []
	# contact_Talia = Contact("Talia", "Trilling", mobile = "2022560512")
	# contact_Michelle = Contact("Michelle", "Choi")
	# contact_Markis = Contact("Markis", "Taylor")
	# contact_list.append(contact_Talia)
	# contact_list.append(contact_Michelle)
	# contact_list.append(contact_Markis)
	for info in contact_list:
		print info.first_name, info.last_name, info.mobile, info.work_number, info.email, info.twitter_handle
	for info in contact_list:
		info.send_text("YO")

if __name__ == '__main__':
	main()

print __name__