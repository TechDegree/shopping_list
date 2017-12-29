# Run the script to start the app
# Put new things one at a time
# Enter DONE - in all caps - to quit the program
# And, once quit, the app should show everything in the list

def show_help():
    print("""
Write what you want to add, and press ENTER / RETURN.

Enter 'DONE' to stop adding items.
Enter 'SHOW' to show what is in your list.     
Enter 'HELP' to show this menu.""")

def show_list():
    for item in shopping_list:
        print(item) 

def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

shopping_list = []
show_help()

while True:
    # ask for new item
    new_item = input("> ")

    # quit adding if DONE
    if new_item == 'DONE':
        break
    # show shopping list
    elif new_item == "SHOW":
        show_list()
        continue
    # show HELP menu
    elif new_item == "HELP":
        show_help()
        continue
    
    # add new item to the list
    add_to_list(new_item)

print("Here is your list: ")
