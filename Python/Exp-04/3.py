import os
import string

path = '/Exp-04/3'
os.chdir(path)
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.writelines(letter)
