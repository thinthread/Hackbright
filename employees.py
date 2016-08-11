# employees.py
# empty list
employee={}

# key value pairs, get user input for height
employee["name"]= "Simone"
employee["age"]= 26
employee["height"]= raw_input(str("Please enter your height: ")).lower()
# update age to a different value
employee["age"]= 36



if "name" in employee:
    print "Key: %s Value: %s" % ("name", employee["name"])
else: print "Key: %s does not exist." % ("name")

# update age to a different value
if 26 in employee:
    print "Key: %s Value: %s" % (26, employee[26])
else: print "Key: %s does not exist." % (26)

# iterate over the key and print each out
for key1 in employee:
    print "%s is a key in employee." % (key1)

# another way to print keys
print employee.keys()

#iterate through and print key:value pairs
for key,value in employee.items():
    print "These are key:value pairs: %s , %s" % (key,value)

print employee























# def value_height():
# 	ht = raw_input(str("please enter your height:")).lower()
# 	actual_height = ""
# 	for ht in employees.items():
# 		if employees["height"]==(ht):
# 			employees["height"] +=1
			

# 	return employees["height"]==(ht)()

# print value_height()