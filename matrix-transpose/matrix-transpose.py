import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    #convert array into numpy array
    A = np.asanyarray(A)
    
    #dimention
    rows, cols = A.shape
    
    # np.indices humein coordinates ki do arrays bana kar deta hai
    i, j = np.indices((cols, rows))
    
    return A[j, i]
    pass
