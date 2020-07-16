# 10. Create numpy array having elements 0 to 10 And negate all the elements between
# 3 and 9
import  numpy as np
arr=np.arange(0,10)
arr[3:9]=np.multiply(arr[3:9], -1)

# Nagated array between 3 to 9
print(arr)