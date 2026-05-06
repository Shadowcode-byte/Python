#3.	Perform Matrix multiplication of any 2 n*n matrices.
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result:\n", result)