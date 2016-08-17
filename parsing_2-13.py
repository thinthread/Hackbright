# my_name="GraceDurham"
# my_name1=list(my_name)
# print my_name1

# numbers="1,2,3,4,5"
# numbers_split=numbers.split(",")
# print numbers_split

# fish_list="One fish two fish red fish blue fish"
# fish_list_split=fish_list.split("fish")
# print fish_list_split

str= "item:apples,quantity:4,price:1.50\n"

split_string=str.split(",")
print split_string

split_string2= split_string[2].split(":")
print split_string2

split_string3=split_string2[1].split(",")
print split_string3

price=float(split_string3[0])
print price 

price1=price=float(split_string3[0])
print price1

split_string4=split_string[1].split(":")
print split_string4

split_string5=split_string4[1].split(",")
print split_string5

quantity=int(split_string5[0])
print quantity

quantity1=quantity=int(split_string5[0])
print quantity1

def calculate_grocery_bill(total):
	total_bill=price1*quantity1

	print total_bill

	# calculate_grocery_bill(total_bill)
print calculate_grocery_bill



