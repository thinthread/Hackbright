str= "item:apples,quantity:4,price:1.50\n"

split_string=str.split(",")
print split_string

split_string2= split_string[2].split(":")
print split_string2

split_string3=split_string2[1].split(",")
print split_string3

price=float(split_string3[0])
print price 


