seq1 = [1, 2, 3, 4, 5]
seq2 = [6, 7, 8, 9, 10]
seq3 = [11, 12, 13, 14, 15]

max_seq = list(map(lambda x, y, z: max(x, y, z), seq1, seq2, seq3))  # map
print(max_seq)

max_seq = list(map(lambda x: max(x), zip(seq1, seq2, seq3)))  # zip
print(max_seq)
