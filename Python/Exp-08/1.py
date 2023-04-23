import numpy as np

arr = np.array([1, 2, 3, 10, 2, 3, 6])

# a
print('Max = ', np.max(arr))
print('Min = ', np.min(arr))

# b
print('Sorted = ', np.sort(arr))

# c
print('Mean = ', np.mean(arr))

# d
'''adding rows'''
array = np.array([[1, 2, 3], [4, 5, 6]])
new_row = np.array([7, 8, 9])
resultant_arr = np.append(array, [new_row], axis=0)
print(resultant_arr)

'''adding columns'''
new_column = np.array([10, 11, 12]).reshape((3, 1))
resultant_arr = np.append(resultant_arr, new_column, axis=1)
print(resultant_arr)

# e
print('Reversed = ', np.flip(arr))

# f
matrix_1 = np.array([[1, 2], [4, 5]])
print(matrix_1)
matrix_2 = np.array([[1, 2], [4, 5]])

print('Multiplication = ', np.multiply(matrix_1, matrix_2))