# Group the data in the dataframe 
import pandas as pd

data = {
    "Player" : ["Kohli","Rohit","ABD","Pat Cummins","Rajat","Yuvi","Rajat"],
    "Rank" : [1,2,4,5,6,3,7],
    "Year" : [2020,2022,2024,2022,2021,2020,2025]
}

df = pd.DataFrame(data)

print("Cricket Players\n",df)

# res= df.groupby('Player')

# for name, group in res :
#     print(f"{name} \n {group}")

# # print("\n",res.first())

print(df.groupby("Player").groups)

