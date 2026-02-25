import numpy as np 

def matrix_addition(A,B):
    return np.add(A,B)

def matrix_mult(A,B):
    return A @ B

def matrix_transpose(A):
    return A.T

def matrix_det(A):
    return np.linalg.det(A)

def matrix_inverse(A):
    return np.linalg.inv(A)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(matrix_addition(A,B))

