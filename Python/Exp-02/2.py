file_name = input("Enter file name: ")
fh = open(file_name)
count = 0
lis = list()
for line in fh:
    line.rstrip()
    word = line.split()
    for j in range(len(word)):
        if word[j].lower() == 'from' and '@' in word[j + 1]:
            lis.append(word[j + 1])
            print(word[j + 1])
            count = count + 1
print(count)
print("There were", count, "mail addresses")
print(lis)
