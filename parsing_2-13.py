# my_name="GraceDurham"
# my_name1=list(my_name)
# print my_name1

# numbers="1,2,3,4,5"
# numbers_split=numbers.split(",")
# print numbers_split

# fish_list="One fish two fish red fish blue fish"
# fish_list_split=fish_list.split("fish")
# print fish_list_split

string= "item:apples,quantity:4,price:1.50\n"

items = ["item:elephants,quantity:4,price:10000.50\n","item:apples,quantity:4,price:1.50\n","item:pears,quantity:5,price:2.00\n","item:cereal,quantity:1,price:4.49\n"]

def calculate_grocery_bill(string):
	split_string=string.split(",")

	split_string2= split_string[2].split(":")

	split_string3=split_string2[1].split(",")

	price=float(split_string3[0])

	price1=price=float(split_string3[0])

	split_string4=split_string[1].split(":")

	split_string5=split_string4[1].split(",")

	quantity=int(split_string5[0])

	quantity1=quantity=int(split_string5[0])


	total_bill=price1*quantity1

	return total_bill

def main(): 
	total_bill=0
	for string in items:
		total_bill = total_bill + calculate_grocery_bill(string)

	print total_bill

main()		


