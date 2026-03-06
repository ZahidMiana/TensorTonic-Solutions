import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Convert input to a NumPy array to handle lists and scalars consistently
    x = np.asanyarray(x, dtype=float)
    
    # Calculate sigmoid: 1 / (1 + exp(-x))
    return 1 / (1 + np.exp(-x))
    pass