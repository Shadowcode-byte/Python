#Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. 
# Also find 2nd maximum element in the array. 
import numpy as np

arr = np.array([[1, 5, 3],
                [8, 2, 7],
                [4, 9, 6]])

print("Array:\n", arr)

# Row-wise sum
print("Row Sum:", np.sum(arr, axis=1))

# Column-wise sum
print("Column Sum:", np.sum(arr, axis=0))

# 2nd maximum
flat = arr.flatten()
flat.sort()
second_max = flat[-2]
print("Second Maximum =", second_max)