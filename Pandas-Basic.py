# ---------- Pandas Basics -----------
import pandas as pd
import numpy as np

df = pd.read_csv('filename.csv')   # Reading in CSV files.
print(df)

# You can select columns with a bracket call
print(df['Name'])
print(df['Salary'])
print(df[['Name','Salary']])

col_names = 'A B C D'.split()
df.columns = ['f1','f2','label']  #to rename the pandas columns

# Similar to NumPy, you can create calls of min(), max(), mean(), 
print(df['Age'].mean())


# Conditional filtering

ser_of_bool = df['Age'] > 30
print(ser_of_bool)

# Use this filter of booleans to then select the rows

age_filter = df['Age'] > 30
print(df[age_filter])

# Or all in one step:
df[df['Age'] > 30]


df['Age'].unique()               # list of unique values for Age
df['Age'].nunique()              # number of unqiue values
df.info()                        # General info about your dataframe
df.describe()                    # Statistics about your dataframe
df.columns                       # Grab a list of all columns
df.index                         # Create an index list
# You can convert a numpy matrix to a dataframe with:
mat = np.arange(50).reshape(5,10)
