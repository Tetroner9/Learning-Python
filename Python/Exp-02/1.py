file_name = input("Enter file name: ")
with open(file_name, 'r') as file:

    # Read the contents of the file and split it into words
    words = file.read().split()

    # Create a set of unique words
    unique_words = set(words)

    # Convert the set to a list and sort it
    sorted_unique_words = sorted(list(unique_words))

    # Print the list of unique words
    print(sorted_unique_words)