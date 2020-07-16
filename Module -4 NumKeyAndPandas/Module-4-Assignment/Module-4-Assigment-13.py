# 13. Create a random array and swap two rows of an array
import numpy as np
randomArray=np.random.randint(0,100,(3,3))
print("Original Array",randomArray)

# Swap rows
randomArray[[0,2]]=randomArray[[2,0]]
print("Swapped Array", randomArray)

