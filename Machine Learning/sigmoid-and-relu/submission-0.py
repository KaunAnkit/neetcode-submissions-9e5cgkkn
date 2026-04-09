import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        k= []
        for x in z:
            y = 1 / (1 + np.exp(-x))
            k.append(np.round(y,5))
            
        return k

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        k =[]

        for x in z:

            k.append(float(max(0,x)))

        return k
