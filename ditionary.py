# ditionary.py

# vocabulary_words={"tuple": "immutable string","concatenate": "add","len": "length","int": "integer",}

# def count_key():
# 	character_dict = {}
# 	name ="stephanieboyette"

# 	for character in name:
# 		if character in character_dict:
# 			character_dict[character] +=1

# 		else:
# 			character_dict[character] =1

# 	return character_dict

# print count_key()

# prices = {
# 	"banana": 4,
# 	"apple": 2, 
# 	"oranages": 1.5, 
# 	"pear": 3
# 	}

def find_expensive_price():
	topValue = 0
	topKey = ""
	for k,v in prices.items():
		if v > topValue:
			topValue = v
			topKey = k

	return topKey

print find_expensive_price()

