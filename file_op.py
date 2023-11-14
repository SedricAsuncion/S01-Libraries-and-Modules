import random
reccomendations = "BookRecomendations.txt" #my developer-defined list

def take_recommendations(which):
    filename = reccomendations
    file = open(filename, "r")
    file_contents = file.readlines()
    file.close()
    titles = len(file_contents) - 2
    if which == "content":
        return file_contents
    elif which == "length":
        return titles
    
#Giving a slice of the recommendations list
def sliced_recommendations(num_elements):
    # Open the file in read mode
    file_contents = take_recommendations("content")

    # Process the file contents
    my_list = [line.strip() for line in file_contents[3:]]  # Slice the list starting from index 3
    #print(my_list)

    random_slice = random.sample(my_list, num_elements)

    formatted_slice = [f"{element}\n" for element in random_slice]
    formatted_output = "".join(formatted_slice)

    print(formatted_output)