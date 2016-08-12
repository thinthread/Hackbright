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

main_lists = {'WF': 'wine, cheese', 'TJ': 'ice cream, cookies', 'SW': 'vitawater, rice'}

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

    

    # menu_prompt={
    #     '0':'Main menu', 
    #     '1':'Show All Lists',
    #     '2':'Show a specific list', 
    #     '3':'Add a new list',
    #     '4':'Add item to list',
    #     '5':'Remove item from list',
    #     '6':'Remove a list by nickname',
    #     '7':'Exit when finished'     
    #     }



def show_all_lists():
   print main_lists.keys()


def show_sorted_list(key):
    # todo:
    pass


def add_new_list(key):
    # add a new list with key as name of the list
    # make sure a list with this name doesn't already exist
    # deal with uppercase/lowercase
    for nickname in main_lists:
        if nickname in main_lists:
            print ""

    pass


def add_item_to_list(key, item):
    # add an item to an existing list
    # make sure the item doesn't already exist
    # deal with uppercase/lowercase
    pass


def remove_item_from_list(key, item):
    # todo:
    pass


def remove_list(key):
    # todo:
    pass


def main():
    
    # this is where the core logic will be
    # start by calling the menu prompt to return the user's choice
    while True: 
        menu_prompt()
       
        selection = int(raw_input("Enter number from menu selection:\n"))

        if selection == 1:
            show_all_lists()

        # if selection == 2:
        #     show_sorted_list(key)

        #  if selection == 3:
        #    add_new_list(key)

        # if selection == 4:
        #     add_item_to_list(key, item)

        # if selection == 5:
        #     remove_item_from_list(key, item)


        # if selection == 6:
        #     remove_list(key)

        # if selection == 7:
        #     break


if __name__ == "__main__":
    main()