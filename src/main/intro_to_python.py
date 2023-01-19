import numpy as np

# 1. Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
# 2. Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j
# 3. Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created

# Create a m x n matrix of zeros
m, n = 3, 3
matrix = np.zeros(shape=(m, n), dtype=int)

# Fill diagonal with 1's
for i in range(m):
    for j in range(n):
        if (i == j):
            matrix[i, j] = 1

print('\nExercise 1\n')
print(matrix)

# Fill non-diagonal with 3's
for i in range(m):
    for j in range(n):
        if (i != j):
            matrix[i, j] = 3

print('\nExercise 2\n')
print(matrix)

# Delete last column
matrix_del = np.delete(matrix, n-1, 1)

print('\nExercise 3\n')
print(matrix_del)
