import file_op
import list_op

## ----- Placeholders -----##
complete_list = list_op.complete_list
reading_list = list_op.reading_books
read_list = list_op.read_books

## ----- Main Code ----- ##
repeat = True
while repeat:
    list_op.nap(2)
    #Navigation system
    valid = True
    while valid:
    #Numeric Validtation
        try:
            action = int(input("What would you like to do?\n 1. Get recommendations\n 2. Read the complete reading list\n 3. Add to a reading list\n 4. Read a reading list\n 5. Remove from a reading list\n 6. Exit\n"))
            if action in [1, 2, 3, 4, 5, 6]:
                valid = False
                break
            else:
                print("\nInput valid choices, not letters\n\n")
                list_op.nap(1)
                valid = True
        except ValueError:
            print("\nInput valid choices, not letters\n\n")
            list_op.nap(1)
            valid = True

    if action ==1:
        list_op.nap(1)
        #How many recommendations
        available = file_op.take_recommendations("length")
        print(f"There are {available} recommendations available.")
        num_elements = int(input("How many titles do you want to generate?"))
        file_op.sliced_recommendations(num_elements)
    if action == 2:
        list_op.nap(1)
        availabe = list_op.length(complete_list)
        print(f"There are {availabe} titles available.")
        num_elements = int(input("How many titles do you want to generate?"))
        list_op.sliced_lists(complete_list, num_elements)        
    elif action == 3:
        list_op.nap(1)
        list = list_op.pick_list()
        list.append(input("What book would you like to add? "))
    elif action == 4:
        list_op.nap(2)
        list = list_op.pick_list()
        availabe = list_op.length(list)
        print(f"There are {availabe} titles available.")
        num_elements = int(input("How many titles do you want to generate?"))
        list_op.sliced_lists(list, num_elements)
    elif action == 5:
        list_op.nap(2)
        list = list_op.pick_list()
        print(list)
        book_to_remove = input("What book would you like to remove? ")
        
        while book_to_remove not in list:
            print("Book not found in the list. Please try again.")
            book_to_remove = input("What book would you like to remove? ")
        list.remove(book_to_remove)
    elif action == 6:
        list_op.nap(2)
        print("Thank you for visiting,\nSee you next time!")
        repeat = False