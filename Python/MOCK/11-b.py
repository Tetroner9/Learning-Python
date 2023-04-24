import pandas as pd

# A
# Create a sample dataframe
data = {'Name': ['John', 'Alice', 'Bob', 'Emily'],
        'Age': [25, 30, 27, 32],
        'Gender': ['Male', 'Female', 'Male', 'Female'],
        'Salary': [50000, 60000, 55000, 70000],
        'Department': ['HR', 'IT', 'Finance', 'Marketing']}
df = pd.DataFrame(data)

# Select specific columns and rows from the dataframe
selected_df = df.loc[[0, 2], ['Name', 'Age', 'Salary']]
print(selected_df)

# B
# Create two sample dataframes
data1 = {'id': [1, 2, 3, 4],
         'name': ['John', 'Alice', 'Bob', 'Emily'],
         'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df1 = pd.DataFrame(data1)

data2 = {'id': [5, 6, 7, 8],
         'name': ['James', 'Linda', 'Michael', 'Sarah'],
         'city': ['San Francisco', 'Seattle', 'Austin', 'Boston']}
df2 = pd.DataFrame(data2)

# Join the two dataframes along rows
merged_df = pd.concat([df1, df2])

# Create another dataframe
data3 = {'id': [1, 3, 5, 7],
         'salary': [50000, 55000, 60000, 65000]}
df3 = pd.DataFrame(data3)

# Merge the merged_df with df3 along the common column id
final_df = pd.merge(merged_df, df3, on='id')
print(final_df)
