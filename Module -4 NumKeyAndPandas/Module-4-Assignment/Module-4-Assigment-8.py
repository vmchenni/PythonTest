# 8. Create a 10x10 array with random values and find the minimum and maximum
# values.
import  numpy as np
randomArray=np.random.randint(0,100,(10,10))
print(randomArray)
print("Minimum Value of Random Array",np.min(randomArray))
print("Maxium Value of Random Array",np.max(randomArray))