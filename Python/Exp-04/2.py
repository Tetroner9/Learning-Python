
lst = list()
paragraph = open('input-2_1.txt', 'r')

for line in paragraph:
    line.rstrip()
    word = line.split()
    for j in word:
        lst.append(j)
print(lst)
paragraph = open('input-2_2.txt', 'r')
lst = list()
for line in paragraph:
    line.rstrip()
    word = line.split()
    for j in word:
        lst.append(j)
print('\n', lst)
