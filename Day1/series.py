import pandas as pd
import numpy as np

data = ["SANJAY","Santu","Hema","KaDLE","chollY","Djs sjdsn JSd dks","k",np.nan]

ss = pd.Series(data)

print("\nSeries data:\n",ss)

print("\Specific value in a series:\n",ss.str.contains("Santu"))