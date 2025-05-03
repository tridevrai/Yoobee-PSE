# Activity W4-2-1: txt file
# Read the txt file and printout the first and last line of the file. See below

import pandas as pd

df = pd.read_csv('./week_3/sample_text.txt', header=None)
print(f"First line: {df.iloc[0,0]}")
print(f"Last line: {df.iloc[-1,0]}") # -1 is shorthand for the last row, 0 is the first column