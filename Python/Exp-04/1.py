with open("input-1.txt") as f:
    lines = f.read()
    words = lines.split()
    wordcount = len(words)
    wordcount = str(wordcount)
    f.close()
with open("output-1.txt", 'w') as f:
    f.write(wordcount)
    f.close()
