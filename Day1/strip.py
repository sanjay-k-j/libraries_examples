import pandas as pd

data = ["!Sanjay\t","Ajay\n\n","\nPuneeth","Suhas\n"]

ser = pd.Series(data)

print("Series :\n",ser)

ser2 = ser.str.rstrip("!\n\t")

print(ser2)
