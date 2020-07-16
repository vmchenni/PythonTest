# 7. Create a numpy array having NaN (Not a Number) and print it.
# array([ nan, 1., 2., nan, 3., 4., 5.])
# Print the same array omitting all elements which are nan
import numpy as np
myarray=([np.NaN, 1, 2,np.NaN, 3, 4, 5])
arr=np.asarray(myarray)
# print(arr)
newArr =arr[~np.isnan(arr)]
# print not Nan array elements
print(newArr)