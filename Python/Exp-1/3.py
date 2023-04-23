string = input("Enter a string: ")

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

modified_string = ''
for char in string:
    if char in vowels:
        modified_string += '*'
    else:
        modified_string += char

print("Modified string:", modified_string)
