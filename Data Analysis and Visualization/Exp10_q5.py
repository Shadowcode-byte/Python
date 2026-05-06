#5Write a Pandas program to get the first 3 rows of a given DataFrame.
import pandas as pd
import numpy as np

exam_data = {
'name': ['Kamal','Don','Ram','Aryan','Virat','Sam','Vaibhav'],
'attempts': [1,3,2,3,2,3,1],
'qualify': ['yes','no','yes','no','no','yes','yes']
}

labels = ['a','b','c','d','e','f','g']

df = pd.DataFrame(exam_data, index=labels)

print("First three rows:\n", df.head(5))