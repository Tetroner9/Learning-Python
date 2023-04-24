def count_words(file_path):
    """Count the number of words in a text file."""
    with open(file_path, 'r') as f:
        text = f.read()
        words = text.split()
        return len(words)


# Example usage
file_path = 'input-4.txt'
num_words = count_words(file_path)
print(num_words)
