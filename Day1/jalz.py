import pandas as pd
import numpy as np

data = {
    "A": [1, 2, np.nan],
    "B": [4, None, 6],
    "C": [7, 8, 9],
}
df = pd.DataFrame(data)

print(df.head())
print("After filling the values")

filled_df = df.fillna(69)
# Filter rows with at least one missing value

print(filled_df)

# rows_with_missing = df[df.isnull().any(axis=1)]
# print(rows_with_missing)



# resDf = df.dropna()

# print("After Dropping\n",resDf.to_string())
