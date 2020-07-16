# 6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements
# greater than 5.
import numpy as np
myarray=[[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]
arr=np.asarray(myarray)
# print(arr)
newArr = arr[arr > 5]
# Print Array Elements Grater than 5
print(newArr)