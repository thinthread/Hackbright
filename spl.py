# spl.py
'''
Code Workshop - Dictionary Shopping list.
This program will do the following.
0 - Main Menu
1 - Show all lists.
2 - Show a specific list. 
3 - Add a new shopping list.
4 - Add an item to a shopping list.
5 - Remove an item from a shopping list.
6 - Remove a list by nickname.
7 - Exit when you are done.
'''

main_list = {
	'WF': ['wine', 'cheese'], 
	'TJ': ['ice cream', 'cookies'], 
	'SW': ['vitawater', 'rice']
	}

def menu_prompt():
    # todo: display menu and get choice using raw_input from user.
    print "Select Option"
    print "0 - Main menu" 
    print "1 - Show all Lists"
    print "2 - Show a specific list" 
    print "3 - Add a new list"
    print "4 - Add item to list"
    print "5 - Remove item from list"
    print "6 - Remove a list by nickname"
    print "7 - Exit when finished"

#1
def show_all_lists():   
   print main_list
#2-2
def show_all_stores():
    current_stores = main_list.keys()
    print "These are your store options!", current_stores
#2-1
def show_sorted_list(store):
    if store in main_list:
        main_list[store] =[]#main_list.values()
        return show_sorted_list[store].keys()#.values()
 # main_list[chosen_list] = []#######################################?????????
    # main_list[chosen_list].values()
    # for values in main_list[chosen_list].sort():
    #     print main_list[chosen_list].value ()
    #     return main_list[chosen_list].values()


#3-1
def add_new_list(nick_name):
    if nick_name not in main_list:
        main_list[nick_name] = []
       	print "%s has been added." % (nick_name)

    else:
        show_all_stores()
        print "This store %s already exists!" % (nick_name)
    return main_list
#3-2
def check_store(store):
    if store not in main_list:
        main_list[store]=[]
        print main_list[store]
#4
def add_item_to_list(item,store):
    for store_list in main_list.values():
        if item in store_list:
            print "%s is already in the list." % (item)
#4        
    show_all_stores()

#4    
    main_list[store].append(item)
    print main_list[store]

#5
def remove_item_from_list(item):
    for store, store_list in main_list.items():
        if item in store_list:
            print store, " and ", store_list
            main_list[store].remove(item)
            print main_list[store]


    print "%s  is not in any list." % (item)
            

#6
def remove_list(store):
    
    del main_list[store]
    

#7
def main():
    
    while True: 

        menu_prompt()
       
        selection = int(raw_input("Enter number from menu selection.:\n"))

    
        if selection == 1:
            show_all_lists()

        if selection == 2:
            chosen_list = raw_input("What store shopping list would you like to see?:\n")
            # print show_sorted_list(chosen_list).values() #??????
            # print show_sorted_list
            show_sorted_list()
            show_all_stores()

        if selection == 3:
           store_name=  raw_input("what store do you want to add?:\n ")
           print add_new_list(store_name)

        if selection == 4:
            new_item =  raw_input("What item do you want to add?:\n")
            add_item_store =  raw_input ("What store list did you want to add the item to?:\n")
            add_item_to_list(new_item, add_item_store)
            
        if selection == 5:
            removed_item = raw_input("What item would you like to remove?:\n")
            remove_item_from_list(removed_item)

        if selection == 6:
            removed_store = raw_input("What store do you want to remove?:\n")
            remove_list(removed_store)
            print main_list

        if selection == 7:
            break



if __name__ == "__main__":
    main()