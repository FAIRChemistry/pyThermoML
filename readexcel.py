import numpy as np
import pandas as pd


df = pd.read_excel("spreadsheet.xlsx", nrows=30)

print(df)

print(df.iloc[5][2])