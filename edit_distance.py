# Compute the edit distance of two strings (minimum number of operations needed to change one string into the other)

import numpy as np

filename = '/Users/jlsta/PycharmProjects/HW_2/HW_2_Files/Edit_distance.txt' # put input file here

with open(filename) as f:
    string_1 = f.readline().strip()
    string_2 = f.readline().strip()

print(string_1, string_2)

# Fast and memory-efficient way to pre-allocate edit distance matrix:
matrix = np.zeros((len(string_1), len(string_2)))
for i in range(len(string_1)):
    matrix[i, 0] = i
for j in range(len(string_2)):
    matrix[0, j] = j

# Calculate edit distance between two string
for j in range(1, len(string_2)):
    for i in range(1, len(string_1)):
        deletion = matrix[i - 1, j] + 1
        insertion = matrix[i, j - 1] + 1
        identity = matrix[i - 1, j - 1] if string_1[i] == string_2[j] else np.inf
        substitution = matrix[i - 1, j - 1] + 1 if string_1[i] != string_2[j] else np.inf
        matrix[i, j] = min(insertion, deletion, identity, substitution)

print(matrix)
