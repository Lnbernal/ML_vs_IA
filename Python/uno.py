import numpy as np
import pandas as p
import flask as f
print("Numpy: ",np.__version__)
print("pandas: ",p.__version__)
print("flask: ",f.__version__)
lista =[1,2,3,4,5]
arr = np.array(lista)
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
