# 11. Create a random array of 3 rows and 3 columns and sort it according to 1st column,
# 2nd column or 3rd column

import numpy as np
randomArray=np.random.randint(0,100,(3,3))

print("Original Array",randomArray)
# np.sort(randomArray.view('i8,i8,i8'), order=['f1'], axis=0).view(np.int)
print("Sorted array by second column", randomArray[randomArray[:,1].argsort()])
print("Sorted array by third column", randomArray[randomArray[:,2].argsort()])


