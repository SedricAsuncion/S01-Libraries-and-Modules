from time import sleep

## ----- Variables ----- ##
read_books = ["Option B", "Eat That Frog", "Building A Second Brain", "Alchemist", "Harry Potter and the Philosopher's Stone"]
reading_books = []
complete_list = [read_books, reading_books] 
def length(lists):
    if lists == complete_list:
        read = len(read_books)
        reading = len(reading_books)
        titles = read + reading

    else:
        titles = len(lists)
    
    return titles

#Printing the complete list, with spaced out books
def sliced_lists(lists, num_elements):
   if lists == complete_list:
       sliced_list = complete_list[:num_elements]
       print("\nBooks in the list:")
       for sublist in sliced_list:
           for title in sublist[:num_elements]:
               print(title)
       
   elif lists == read_books:
       sliced_list = read_books[:num_elements]
       print("\nBooks I've read:")
       for title in sliced_list:
            print(title)
       
   elif lists == reading_books:
       sliced_list = reading_books[:num_elements]
       print("\nBooks I'm reading:")
       for title in sliced_list:
            print(title)
        
#Picking which list to view or remove from
def pick_list():
    valid = True
    while valid:
        try:
                pick = int(input("Which list would you like pick? 1. Reading list 2. Finished list\n"))
                if pick == 1:
                    list = reading_books      
                    valid = False      
                elif pick == 2:
                    list = read_books
                    valid = False
                else:
                    print("\nInput valid choices, not letters\n\n")
                    valid = True

        except ValueError:
            print("\nInput valid choices, not letters\n\n")
            valid = True        
    return list
        
def nap(t):
    print("Loading...")
    sleep(t)
    