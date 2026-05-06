#Write a Pandas program to get the powers of an array values element-wise. 
import pandas as pd

data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)
power_df = df*df   
print("\nAfter Power:\n", power_df)
