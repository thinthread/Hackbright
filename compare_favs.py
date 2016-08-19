my_file = "michelle_fav_foods.txt"
pair_file = "stephanie_fav_fods.txt"

def read_file_to_list(my_file):
	with open (my_file) as my_file:
		output_list = my_file.readlines()
	return output_list

def read_file_to_new_list(pair_file):
	with open (pair_file) as pair_file:
		output_list2 = pair_file.readlines()
	return output_list2

def compare_favs(my_file,pair_file):
	
	for i in range(len(my_file)):

		if my_file[i].strip()!= pair_file[i].strip():	
			return "Our favs are different!"

		else:
			return "Our favs are the same!"
	

def main():
	output_list = read_file_to_list(my_file) 
	output_list2 = read_file_to_new_list(pair_file)
	print output_list
	print output_list2
	print compare_favs(output_list,output_list2)

main()