import pandas as pd
# a
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

print('Addition: ', s1 + s2)
print('Subtraction: ', s1 - s2)
print('Multiplication: ', s1 * s2)
print('Division: ', s1 / s2)

# b
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

first_column_series = df['A']
print("First column as a Series (using indexing):")
print(first_column_series)

# c
df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [5, 6, 7, 8],
                   'C': [9, 10, 11, 12],
                   'D': [13, 14, 15, 16]})

selected_columns = df[['A', 'C']]
print("Selected columns:")
print(selected_columns)

selected_rows = df[1:3]
print("\nSelected rows:")
print(selected_rows)

selected_columns_and_rows = df.loc[1:2, ['B', 'D']]
print("\nSelected columns and rows:")
print(selected_columns_and_rows)

# d
df = pd.DataFrame({'StudentID': [101, 102, 103, 104, 105],
                   'Attempts': [3, 4, 2, 5, 1]})

sum_attempts = df.groupby('StudentID')['Attempts'].sum()

print("Sum of examination attempts by students:")
print(sum_attempts)

# e

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6]})

print("Original DataFrame:")
print(df)

dict_list = [{'A': 4, 'B': 7},
             {'A': 5, 'B': 8}]

df_to_append = pd.DataFrame(dict_list)

df = pd.concat([df, df_to_append], ignore_index=True)

print("\nDataFrame after appending list of dictionaries:")
print(df)

new_series = pd.Series({'A': 6, 'B': 9})

df = pd.concat([df, new_series], axis=1)

print("\nDataFrame after appending Series:")
print(df)


# f

df1 = pd.DataFrame({'id': [1, 2, 3],
                    'A': ['a1', 'a2', 'a3'],
                    'B': ['b1', 'b2', 'b3']})

df2 = pd.DataFrame({'id': [4, 5, 6],
                    'A': ['a4', 'a5', 'a6'],
                    'B': ['b4', 'b5', 'b6']})

df3 = pd.DataFrame({'id': [2, 3, 6],
                    'C': ['c2', 'c3', 'c6'],
                    'D': ['d2', 'd3', 'd6']})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nDataFrame 3:")
print(df3)

joined_df = pd.concat([df1, df2], ignore_index=True)

print("\nJoined DataFrame (df1 and df2):")
print(joined_df)

merged_df = pd.merge(joined_df, df3, on='id')

print("\nMerged DataFrame (joined_df and df3):")
print(merged_df)