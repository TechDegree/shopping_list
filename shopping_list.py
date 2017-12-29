# Run the script to start the app
# Put new things one at a time
# Enter DONE - in all caps - to quit the program
# And, once quit, the app should show everything in the list

shopping_list = []

print("What would you like to add?")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new item
    new_item = input("> ")

    # quit adding if DONE
    if new_item == 'DONE':
        break
    # show shopping list
    elif new_item == "SHOW":
        for item in shopping_list:
            print(item)
        continue
    # show HELP menu
    elif new_item == "HELP":
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'SHOW' to show what is in your list.")         
        print("Enter 'HELP' to show this menu.")         
        continue
    
    # add new item to the list
    shopping_list.append(new_item)

print("Here is your list: ")

for item in shopping_list:
    print(item) 