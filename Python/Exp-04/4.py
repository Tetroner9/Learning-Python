import string


def count_alphabets(filename):
    with open(filename, 'r') as file:
        contents = file.read().lower()
        alphabet = list(string.ascii_lowercase)
        lettercount = {words: 0 for words in alphabet}
        for char in contents:
            if char in alphabet:
                lettercount[char] += 1
        return lettercount


alphabet_counts = count_alphabets('input-4.txt')
for letter, count in alphabet_counts.items():
    print(f"{letter}: {count}")
