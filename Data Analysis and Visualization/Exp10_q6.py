#Write a Pandas program to find and replace the missing values 
#in a given DataFrame which do not have any valuable information.
import pandas as pd
import numpy as np

df = pd.DataFrame({

})

print("Original:\n", df)

# Replace missing values with 0
df.fillna(0, inplace=True)

print("\nAfter replacing missing values:\n", df)